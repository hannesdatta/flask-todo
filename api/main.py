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
        return(out)
    else:
        return({'success': False})


@app.post("/user.setinfo/")
async def user_setinfo(request: Request):
    obj = await request.json()

    user_id = obj.get('user_id')

    user = users.search(where('id') == user_id)

    if (len(user)>0):
        # exists
        nickname = obj['nickname']

        print('user exists')
        users.update({'nickname': nickname,
                      'changed': get_timestamp()},
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

    c=course[0] #return(course[0])

    # retrieve module
    if c.get('modules') is None: return(c)

    # all_task_ids
    all_task_ids = []
    mod_tasks = {}
    for m in range(len(c['modules'])):
        tmp_tasks = []
        for cat in c['modules'][m].get('items'):
            for task in cat.get('items'):
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
        query = """SELECT COUNT(DISTINCT user_id) as users, SUM(user_id == """+str(user_id)+""") as user_completion FROM events WHERE
        task_id IN (""" + ','.join(task_ids) + """) AND status = 1 AND type = "completed";"""
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
