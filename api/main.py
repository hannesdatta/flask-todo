from typing import Optional

from fastapi import FastAPI, Request
from tinydb import TinyDB, Query, where
import math
from datetime import datetime, timedelta
from random import random
from werkzeug.security import generate_password_hash, check_password_hash
from name import random_nickname
import time
from starlette.requests import Request
from databases import Database
import asyncio
import pandas as pd

# Open databases

## NoSQL
db = TinyDB('db.json')

courses = db.table('courses')
users = db.table('users')
conversations = db.table('conversations')
status = db.table('status')

# SQL
database = Database('sqlite:///events_comments.db')

# Create API
app = FastAPI()


# FUNCTIONS TO CREATE DATABASE
# ============================

@app.get("/create")
async def create_data():
    # Create a table.
    query = """CREATE TABLE events (user_id INTEGER NOT NULL,
                                    task_id VARCHAR(24) NOT NULL,
                                    type VARCHAR(12) NOT NULL,
                                    timestamp INTEGER NOT NULL,
                                    status INT,
                                    PRIMARY KEY(user_id, task_id, type, timestamp))"""
    await database.execute(query=query)

@app.get("/create_comments")
async def create_data2():
    # Create a table.

    query = """CREATE TABLE comments (id INTEGER PRIMARY KEY,
                                    user_id INTEGER NOT NULL,
                                    task_id VARCHAR(24) NOT NULL,
                                    timestamp INTEGER NOT NULL,
                                    parent INTEGER,
                                    text TEXT)"""
    query2 = """CREATE INDEX task_index ON comments (task_id);"""

    try:
        await database.execute(query=query)
    except:
        print('cannot create comments')
    try:
        await database.execute(query=query2)
    except:
        print('cannot create index on comments')

@app.get("/create_logs")
async def create_data3():
    # Create a table.

    query = """CREATE TABLE logs (id INTEGER PRIMARY KEY,
                                    user_id NOT NULL,
                                    timestamp INTEGER NOT NULL,
                                    task_id VARCHAR(24),
                                    type TEXT)"""
    query2 = """CREATE INDEX log_index ON logs (task_id);"""

    try:
        await database.execute(query=query)
    except:
        print('cannot create logs')
    try:
        await database.execute(query=query2)
    except:
        print('cannot create index on logs')

# AUXILARY FUNCTIONS
# ==================

def get_timestamp():
    return(math.floor(time.time()))


# API ENDPOINTS
# =============

@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/export")
async def fetch_data():#id: int):
    query = "SELECT * FROM events"
    results = await database.fetch_all(query=query)
    return  results

@app.get("/user.set_tasks/")
async def user_settask(user_id: int, task_id: str,
                       type: str,
                       status: int):
    timest = get_timestamp()


    query = "INSERT INTO events(user_id, task_id, type, timestamp, status) VALUES (:user_id, :task_id, :type, :timestamp, :status)"


    values = [
            {"user_id": user_id, "task_id": task_id, "type": type,
            'timestamp': timest, "status": status}
        ]

    await database.execute_many(query=query, values=values)


@app.get("/insert")
async def insert():
    import time
    timest = math.floor(time.time())
    query = "INSERT INTO events(user_id, task_id, timestamp, type, status) VALUES (:user_id, :task_id, :timestamp, :type, :status)"
    values = [
        {"user_id": 1, "task_id": "x1", "type": "completed",
        'timestamp': timest, "status": 1},
        {"user_id": 1, "task_id": "x2", "type": "explain",
        'timestamp': timest, "status": 1},
        {"user_id": 2, "task_id": "x2", "type": "explain",
        'timestamp': timest, "status": 1}
    ]

    await database.execute_many(query=query, values=values)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/user.info/{user_id}")
def user_getinfo(user_id):
    user = users.search(where('id') == int(user_id))
    print(user)
    if (len(user)>0):
        out = user[0]
        out['success'] = True

        try:
            out['use_leaderboard']
        except:
            out['use_leaderboard'] = True
        return(out)
    else:
        return({'success': False})

@app.get("/user.search/")
async def user_getinfo(query: str):
    import re
    print(query)
    query = query.replace('"','')
    query = '.*'+query+ '.*'
    User = Query()
    return(users.search(User.email.matches(query, flags=re.IGNORECASE)))


@app.post("/user.setinfo/")
async def user_setinfo(request: Request):
    obj = await request.json()

    user_id = obj.get('user_id')

    user = users.search(where('id') == user_id)

    if (len(user)>0):
        # exists
        nickname = obj['nickname']
        use_leader = True
        try:
            use_leader = obj['use_leaderboard']
        except:
            1+1

        msg = ''
        try:
            msg = obj['leaderboard_message']
        except:
            1+1

        users.update({'nickname': nickname,
                      'changed': get_timestamp(),
                      'use_leaderboard': use_leader,
                      'leaderboard_message': msg},
                     where('id') == user_id)

    else:
        return({'status':999, 'msg': 'user does not exist!'})

    return {'status':200}

@app.post("/logging/")
async def logging(request: Request):
    obj = await request.json()

    timest = get_timestamp()
    user_id = obj.get('user_id')
    task_id = obj.get('task_id')
    type = obj.get('type')

    query = "INSERT INTO logs(user_id, task_id, timestamp, type) VALUES (:user_id, :task_id, :timestamp, :type)"

    values = [
            {"user_id": user_id, "task_id": task_id,
            'timestamp': timest, "type": type}
        ]

    await database.execute_many(query=query, values=values)

    return {'status':200}


@app.get("/user.get_modules/{user_id}/{course_id}")
def user_getmodules(user_id,course_id):
    course = courses.search(where('id') == int(course_id))
    return(course[0])

@app.get("/user.get_courses")
async def user_getcourses(user_id: int):
    all_courses = courses.all()

    queries = []
    for c in all_courses:
        all_task_ids = []
        for m in range(len(c['modules'])):
            tmp_tasks = []
            for cat in c['modules'][m].get('items'):
                for task in cat.get('items'):
                    all_task_ids.append('"'+task.get('id')+'"')

        query = """SELECT COUNT(DISTINCT user_id) as users, SUM(user_id == """+str(user_id)+""") as user_completion FROM events WHERE
        task_id IN (""" + ','.join(all_task_ids) + """) AND status = 1 AND type = "completed";"""

        queries.append(query)

    async def generate_url(query):
        results = await database.fetch_one(query=query)
        return results

    learners = await asyncio.gather(*[generate_url(i) for i in queries])

    for i in range(len(learners)):
        all_courses[i]['stats']=learners[i]

    return(all_courses)


@app.get("/comments/show/")
async def show_comments(request: Request, task_id: str=None, user_id: int=None):
    if task_id is None:
        query = """SELECT * FROM comments"""
        # WHERE task_id = """""+ task_id + """"""""
    else:
        query = "SELECT * FROM comments WHERE task_id = \""+ task_id + "\""


    results = await database.fetch_all(query=query)
    print(type(results))

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d

    res = []
    for resu in results:
        print(type(resu))

        out=dict(resu)
        out['user_nickname'] = 'hannes'
        res.append(out)

    return(res)

@app.get("/comments/delete/")
async def del_comments(request: Request, comment_id: int):
    query = "DELETE FROM comments WHERE id = " + str(comment_id)
    results = await database.execute(query=query)
    return {'status':200}

@app.post("/comment/")
async def create_item(request: Request):
    obj = await request.json()

    timest = get_timestamp()
    user_id = obj.get('user_id')
    task_id = obj.get('task_id')
    text = obj.get('text')

    query = "INSERT INTO comments(user_id, task_id, timestamp, text) VALUES (:user_id, :task_id, :timestamp, :text)"

    values = [
            {"user_id": user_id, "task_id": task_id,
            'timestamp': timest, "text": text}
        ]

    await database.execute_many(query=query, values=values)

    return {'status':200}



@app.get("/user.get_tasks/")
async def user_gettoken(user_id: int, module_id: int, request: Request):
    course = courses.all()

    # retrieve module
    mod = {}
    for c in course:
        if c.get('modules') is not None:
            for m in c.get('modules'):
                if m.get('id')==int(module_id):
                    mod = m
                    mod['course_id'] = c.get('id')
                    mod['course_name'] = c.get('name')
                    #return(m)

    # check for task completeness
    task_ids = []
    stats_dic = {}
    for cat in mod.get('items'):
        for task in cat.get('items'):
            stats_dic[task.get('id')] = {'stat_completed': 0,
                                         'stat_explain': 0,
                                         'stat_example':0,
                                         'stat_practice': 0,
                                         'stat_givehelp': 0,
                                         'stat_comments': 0,
                                         'completed': False,
                                          'explain': False,
                                          'example':False,
                                          'practice': False,
                                          'givehelp': False,
                                          'comments': False,
                                          'updated_comments': 0,
                                          'user_viewed': 0
                                          }
            task_ids.append("'"+task.get('id')+"'")

    # select all most recent user-specific events (e.g., completitions)

    query = """SELECT * FROM events, (SELECT user_id, task_id, type, max(timestamp) as max_timestamp
    FROM events WHERE
    task_id IN (""" + ','.join(task_ids) + """) GROUP BY user_id, task_id, type) max_user WHERE
    events.user_id=max_user.user_id AND events.task_id = max_user.task_ID AND
    events.type = max_user.type AND events.timestamp = max_user.max_timestamp"""

    results = await database.fetch_all(query=query)

    # select timestamp of most recent comment
    query2 = """SELECT task_id, COUNT(*) AS count, max(timestamp) as max_timestamp FROM comments WHERE
    task_id IN (""" + ','.join(task_ids) + """) GROUP BY task_id;"""

    results_comments = await database.fetch_all(query=query2)
    #print(results_comments)

    # select timestamp of most recent view event
    query3 = """SELECT task_id, max(timestamp) as max_timestamp FROM logs WHERE
    task_id IN (""" + ','.join(task_ids) + """) AND user_id = """ + str(user_id) + """ GROUP BY task_id;"""

    results_logging = await database.fetch_all(query=query3)
    print(results_logging)

    # build statistics (completed, explain, etc.)
    for r in results:
        if r['type'] in ['completed','explain','example','practice','givehelp']:
            if r['status']==1:
                stats_dic[r['task_id']]['stat_'+r['type']]=stats_dic[r['task_id']]['stat_'+r['type']]+1
                if r['user_id']==user_id:
                    stats_dic[r['task_id']][r['type']]=True

    # build statistics (comments)
    for r in results_comments:
        stats_dic[r['task_id']]['stat_comments'] = r['count']
        stats_dic[r['task_id']]['updated_comments'] = r['max_timestamp']

    # build statistics (comments)
    for r in results_logging:
        stats_dic[r['task_id']]['user_viewed'] = r['max_timestamp']


    for i in range(len(mod['items'])):
        for j in range(len(mod['items'][i]['items'])):
            mod['items'][i]['items'][j]['stats']=stats_dic[mod['items'][i]['items'][j]['id']]

    return(mod)


@app.get("/user.gettoken/")
async def user_gettoken(email: str, request: Request):
    user = users.search(where('email') == email)
    # set next user id
    max_id=0
    for u in users.all():
        if (u['id']>max_id): max_id=u['id']

    token = str(math.ceil(random()*1E6))+'researchcloud'
    hashed_token = generate_password_hash(token, method = 'sha256')[7:]

    now = datetime.utcnow()
    expiry = (now + timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')

    timestamp = get_timestamp()

    if (len(user)>0):
        # user exists, update login token
        print('user exists')
        users.update({'expiry': expiry,
                      'token': hashed_token},
                     where('email') == email)

        return({'token': hashed_token,
                'new': 'False',
                'success': 'True'})

    else:
        print('new user')
        users.insert({'email': email,
                      'nickname': random_nickname(),
                      'name': '',
                      'expiry': expiry,
                      'created': timestamp,
                      'changed': timestamp,
                      'token': hashed_token,
                      'id': max_id+1})

        return({'token': hashed_token,
                'new': 'True',
                'id': max_id+1,
                'success': 'True'})

@app.get("/user.checktoken/{token}")
def user_checktoken(token):
    token = users.search(where('token') == token)
    print(token)
    now = datetime.utcnow()
    print(len(token))
    if (len(token)>0):
        #remember = False
        remember = True
        expiry = datetime.strptime(token[0]['expiry'], '%Y-%m-%d %H:%M:%S')
        print(expiry)
        print(now)
        if now<expiry:
            return({'success': True,
                    'email': token[0]['email'],
                    'id': token[0]['id']})

        #user = User.query.filter_by(email=email).first()
        #now = datetime.utcnow()
    return({'success':False})


async def get_module_data(user_id: int, course_id: int):
    course = courses.search(where('id') == int(course_id))

    c=course[0]

    # retrieve module
    if c.get('modules') is None: return(c)

    # all_task_ids
    all_task_ids = []
    mod_tasks = {}
    for m in range(len(c['modules'])):
        tmp_tasks = []
        for cat in c['modules'][m].get('items'):
            for task in cat.get('items'):
                 try:
                     is_optional = task.get('optional')
                 except:
                     is_optional = False
                 if (is_optional==True): continue
                 all_task_ids.append('"'+task.get('id')+'"')
                 tmp_tasks.append('"'+task.get('id')+'"')
        mod_tasks[c['modules'][m]['id']] = tmp_tasks

    # Query for most recent comments by task
    query2 = """SELECT task_id, COUNT(*) AS count, max(timestamp) as max_timestamp FROM comments WHERE
    task_id IN (""" + ','.join(all_task_ids) + """) GROUP BY task_id;"""

    results_comments = await database.fetch_all(query=query2)

    # select timestamp of most recent view event
    query3 = """SELECT task_id, max(timestamp) as max_timestamp FROM logs WHERE
    task_id IN (""" + ','.join(all_task_ids) + """) AND user_id = """ + str(user_id) + """ GROUP BY task_id;"""

    results_logging = await database.fetch_all(query=query3)

    queries = []
    for key, task_ids in mod_tasks.items():
        print(key)
        print(task_ids)
        # If value satisfies the condition, then store it in new_dict
        # Query for learners

        query = """SELECT COUNT(DISTINCT events.user_id) as users, SUM(events.user_id == """+str(user_id)+""") as user_completion FROM
        (SELECT user_id, task_id, MAX(timestamp) AS created_at FROM events WHERE
        task_id IN (""" + ','.join(task_ids) + """) AND type = "completed"
        GROUP BY user_id, task_id) AS latest_data INNER JOIN
        events ON events.user_id = latest_data.user_id AND
        events.task_id = latest_data.task_id AND
        events.timestamp = latest_data.created_at WHERE status = 1;
        """

        queries.append(query)
        #print(query)

    import asyncio

    async def generate_url(query):
        results = await database.fetch_one(query=query)
        return results

    #for future in asyncio.as_completed(map(fetch, urls)):
    #    result = await future

    tasks = await asyncio.gather(*[generate_url(i) for i in queries])
    #tasks = [generate_url(query) for query in queries]
    #await asyncio.wait(tasks)

    #tasks
    results_status={}
    cnt=0
    for key, task_ids in mod_tasks.items():
        results_status[key] = tasks[cnt]
        cnt+=1

    return({'comments': results_comments,
            'logging': results_logging,
            'status': results_status,
            'course': c})

@app.get("/user.get_module_completition/")
async def user_get_module_completition(user_id: int, course_id: int):
    user_id=int(user_id)
    course_id=int(course_id)

    call = await get_module_data(user_id, course_id)

    results_comments=call['comments']

    results_logging=call['logging']
    results_status=call['status']
    c=call['course']

    # populate json for website
    def analyze_modules(m):
        modid = m.get('id')
        print(modid)
        # Collect all task ids belonging to the module
        task_ids = []

        for cat in m.get('items'):
            for task in cat.get('items'):
                task_ids.append('"'+task.get('id')+'"')

        # Query for learners
        results = results_status[modid]

        comments_dic = {}
        for task in task_ids:
            comments_dic[task.replace('"','')] = {'recent_comment':0,
                                  'recent_view': 0,
                                  'comment_count':0}

        for r in results_comments:
            if '"'+r['task_id']+'"' not in task_ids: continue
            comments_dic[r['task_id']]['recent_comment'] = r['max_timestamp']
            comments_dic[r['task_id']]['comment_count'] = r['count']

        for r in results_logging:
            if '"'+r['task_id']+'"' not in task_ids: continue
            comments_dic[r['task_id']]['recent_view'] = r['max_timestamp']

        new_comment = 0
        comment_count = 0

        for key, value in comments_dic.items():
             # If value satisfies the condition, then store it in new_dict
             com = value
             if com['recent_comment']>com['recent_view']: new_comment+=1
             comment_count+=com['comment_count']

        if new_comment>0:
            flag_new_comment= True
        else:
            flag_new_comment = False

        user_completion = results['user_completion']
        if user_completion is None: user_completion = 0

        try:
            completion_rate = int(round(100 * user_completion/len(task_ids),0))
        except:
            completion_rate = 0

        stats = {#'task': task_ids,
                'users': results['users'],
                'ncompleted': user_completion,
                'ntasks': len(task_ids),
                'sharecompleted': completion_rate,
                'has_new_comments': flag_new_comment,
                'comment_count': comment_count,
                #'res': results_comments,
                #'res2': results_logging,
                #'recency': comments_dic
                }
        return(stats)

    newlist = [analyze_modules(x) for x in c['modules'] ]

    for number in range(len(newlist)):
        c['modules'][number]['stats']=newlist[number]

    return(c)

# cycles through a JSON course object and returns a list of
# to do IDs
def get_tasks(c):
    # all_task_ids
    all_task_ids = []
    mod_tasks = []
    for m in range(len(c['modules'])):
        tmp_tasks = []
        for cat in c['modules'][m].get('items'):
            for task in cat.get('items'):
                 try:
                     is_optional = task.get('optional')
                 except:
                     is_optional = False
                 if (is_optional==True): continue
                 all_task_ids.append('"'+task.get('id')+'"')
                 tmp_tasks.append('"'+task.get('id')+'"')
                 mod_tasks.append({'task_id': task.get('id'),
                                   'task_id_str': '"'+task.get('id')+'"',

                                   'module_id': c['modules'][m].get('id'),
                                   'course_id': c.get('id'),
                                   'optional': is_optional})

    return({'all_tasks': all_task_ids,
            'tasks_by_module' : mod_tasks})

@app.get("/course.get_experience/")
async def experience(course_id: int):
    course = courses.search(where('id') == int(course_id))

    c=course[0]

    # gather relevant task IDs
    call = get_tasks(c)

    all_tasks = call['all_tasks']

    task_modules = pd.DataFrame.from_dict(call['tasks_by_module'])

    #print(df)
    # needs to be like an event table
    # timestamp | activity | type | relations | points

    exp = []

    # initialize experience dict
    my_users = []
    for u in users.all():
        my_users.append(u['id']) #exp[str(u['id'])] = []

    #######################################
    # entire history of to dos with dates #
    #######################################

    query = """SELECT events.*, DATE(timestamp, 'unixepoch') AS isodate FROM
    (SELECT user_id, task_id, MAX(timestamp) AS created_at FROM events WHERE
    task_id IN (""" + ','.join(all_tasks) + """)
    GROUP BY user_id, task_id) AS latest_data INNER JOIN
    events ON events.user_id = latest_data.user_id AND
    events.task_id = latest_data.task_id AND
    events.timestamp = latest_data.created_at WHERE status = 1;
    """

    db_results = await database.fetch_all(query=query)
    #return(results_comments)
    # implement LIKES on comments

    tmp = pd.DataFrame(db_results)
    df=tmp.set_axis(['user_id','task_id','type','unix','status','date'], 'columns')

    df['rank'] = df.groupby("task_id")['unix'].rank("dense", ascending=True)


    ntasks=task_modules.groupby('module_id').agg(
        ntasks_all = ('task_id', 'nunique'))
    ntasks_mandatory=task_modules[task_modules['optional']==False].groupby('module_id').agg(
        ntasks_mandatory = ('task_id', 'nunique'))

    #print(ntasks)
    #ntasks= task_modules.groupby('module_id')['task_id'].nunique()


    df = pd.merge(df, task_modules, on = 'task_id', how = 'left')
    df = pd.merge(df, ntasks, on = 'module_id', how = 'left')
    df = pd.merge(df, ntasks_mandatory, on = 'module_id', how = 'left')

    # user completition
    usercompl=df[(df['type']=='completed') & (df['optional']==False)].groupby(['course_id', 'module_id', 'user_id']).agg(
        completed = ('task_id', 'nunique'),
        completion_time = ('unix', 'max'))

    df = pd.merge(df, usercompl, on = ['course_id', 'module_id', 'user_id'], how = 'left')

    completion_rank=df[(df['completed']==df['ntasks_mandatory'])].groupby(['course_id', 'module_id', 'user_id']).agg(
        unix = ('unix', 'max'),
        date = ('date', 'max'))

    completion_rank['rank'] = completion_rank.groupby(['course_id', 'module_id'])['unix'].rank("dense", ascending=True)
    completion_rank['status'] = 1
    completion_rank['task_id'] = 'module'
    #df = pd.merge(df, completion_rank, on = ['course_id', 'module_id', 'user_id'], how = 'left')

    # help others
    #userhelp=df[(df['type']=='givehelp') & (df['optional']==False) & (df['status']==1)].groupby(['course_id', 'module_id', 'user_id']).agg(
    #    nhelpothers = ('task_id', 'nunique'),
    #    unix = ('unix', 'max'),
    #    date = ('date', 'max'))

    #print(userhelp)
    #c#ompletion_rank['module_completion'] = completion_rank.groupby(['course_id', 'module_id']).agg(
    #    module_completion_rank = ('unix', 'rank'))


#agg_data.sort_values(by=['xp'], inplace=True, ascending = False)

    print(completion_rank)

#    print(df)
    #print(test)

    ##########################
    # SUMMARY OF COMMENTS    #
    ##########################

    query = """SELECT user_id, task_id, MIN(timestamp), DATE(MIN(timestamp), 'unixepoch'), COUNT(*) as ncomments FROM
    comments WHERE
    task_id IN (""" + ','.join(all_tasks) + """) GROUP BY user_id, task_id;
    """

    db_results2 = await database.fetch_all(query=query)
    #return(results_comments)
    # implement LIKES on comments

    tmp = pd.DataFrame(db_results2)
    tmp=tmp.set_axis(['user_id', 'task_id','unix','date', 'count'], 'columns')

    df_comments = pd.merge(tmp, task_modules, on = 'task_id', how = 'left')
    df_comments['status'] = 1
    #df['rank'] = df.groupby("task_id")['unix'].rank("dense", ascending=True)

    #print(df_comments)
    # merge modules


    def combine_ids(x):
        return(';'.join(list(set(x))))

    def calc_experience(df, type, xp, multiplied=True):
        agg_data = df.groupby(['user_id', 'date']).agg(
            unix_min = ('unix', 'min'),
            status_count = ('status', 'sum'),
            tasks = ('task_id', combine_ids))

        for index, row in agg_data.iterrows():
            uid=index[0]
            #if uid not in my_users: continue
            if (multiplied==False): tot_xp = xp
            if (multiplied==True): tot_xp = int(row['status_count']) * xp

            exp.append({'date': index[1],
                        'user_id': uid,
                                             'unix': int(row['unix_min']),
                                             'type': type,
                                             'value': int(row['status_count']),
                                             'xp': tot_xp})
    # daily activity
    calc_experience(df, type = 'daily_activity', xp = 50)

    # mark to do as complete
    calc_experience(df[df['type']=='completed'], type = 'complete_to_do', xp = 30)

    # among first 3 to complete
    calc_experience(df[(df['type']=='completed') & (df['rank']<=3)],
                    type = 'complete_to_do_top3',
                    xp = 30)

    # among first 10 to complete
    calc_experience(df[(df['type']=='completed') & (df['rank']>3) & (df['rank']<=10)],
                    type = 'complete_to_do_top10',
                    xp = 15)

    # receiving likes on a comment


    # mark to do with "can help others"
    calc_experience(df[(df['type']=='givehelp')],
                    type = 'help_others',
                    xp = 10)

    # complete all to dos from a given week
    calc_experience(completion_rank,
                    type = 'complete_module',
                    xp = 50)

    # among first 3 to complete all to dos from a given week
    calc_experience(completion_rank[completion_rank['rank']<=3],
                    type = 'complete_module_top3',
                    xp = 100)

    # among first 10 to complete all to dos from a given week
    calc_experience(completion_rank[(completion_rank['rank']<=10) & (completion_rank['rank']>3)],
                    type = 'complete_module_top10',
                    xp = 50)

    # receive 5 or more likes on a comment


    # mark 3 or more to dos from one week with "can help others"


    # write comment on a to do
    calc_experience(df_comments[df_comments['count']>0],
                    type = 'write_comment',
                    xp = 20)

    # mark 10 or more to dos with can help others in total


    #print(df_comments)
    return(exp)

    # experience logs


@app.get("/course.get_leaderboard/")
async def leaderboard(course_id: int, timestamp: int = get_timestamp()):
    exp_data = await experience(course_id)
    df = pd.DataFrame.from_dict(exp_data)

    agg_data = df.groupby(['user_id']).agg(
        xp = ('xp', 'sum'),
        last_activity = ('unix', 'max'))

    agg_data.sort_values(by=['xp'], inplace=True, ascending = False)

    leaderboard = []

    course = courses.search(where('id') == course_id)

    rank=1
    for index, row in agg_data.iterrows():
        uid=index

        user = users.search(where('id') == uid)
        print(user)

        try:
            use_leaderboard = user[0]['use_leaderboard']
        except:
            use_leaderboard = True

        if (use_leaderboard==False): continue

        try:
            nickname = user[0]['nickname']
        except:
            nickname = 'Anonymous user'

        try:
            leaderboard_message = user[0]['leaderboard_message']
        except:
            leaderboard_message = 'No status message'

        leaderboard.append({'rank': rank,
                            'user_id': uid,
                            'nickname': nickname,
                            'xp': int(row['xp']),
                            'last_activity': friendly_time(int(row['last_activity'])),
                            'leaderboard_message': leaderboard_message})
        rank+=1


    # populate nicknames

    return({'leaderboard': leaderboard,
            'course': {'name': course[0]['name'],
            'id': course[0]['id']}})


def friendly_time(unix):
    from datetime import datetime

    ts_date=datetime.utcfromtimestamp(unix).strftime('%d-%m-%Y')
    ts_time=datetime.utcfromtimestamp(unix).strftime('%H:%M')

    timestamp_printable = ts_date + ' at ' + ts_time
    if (datetime.utcnow().strftime('%d-%m-%Y'))==ts_date: timestamp_printable = 'Today at ' + ts_time
    if str(int((datetime.utcnow().strftime('%d')))-1)+(datetime.utcnow().strftime('-%m-%Y'))==ts_date: timestamp_printable = 'Yesterday at ' + ts_time

    return(timestamp_printable)
