from typing import Optional

from fastapi import FastAPI, Request
from tinydb import TinyDB, Query, where
import math
from datetime import datetime, timedelta
from random import random
from werkzeug.security import generate_password_hash, check_password_hash
from name import random_nickname
import time


def get_timestamp():
    return(math.floor(time.time()))


from databases import Database
database = Database('sqlite:///events_comments.db')

app = FastAPI()


@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/test")
async def fetch_data():#id: int):
    query = "SELECT * FROM events" # WHERE ID={}".format(str(id))
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


            #processstat('checked', 'completed')
            #processstat('explain', 'explain')
            #processstat('example', 'example')
            #processstat('practice', 'practice')
            #processstat('givehelp', 'givehelp')



    await database.execute_many(query=query, values=values)


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

    await database.execute(query=query)
    await database.execute(query=query2)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


db = TinyDB('db.json')

courses = db.table('courses')
users = db.table('users')
conversations = db.table('conversations')
status = db.table('status')


from starlette.requests import Request

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




@app.get("/user.get_courses/{user_id}")
def user_getcourses(user_id):
    return(courses.all())

@app.get("/user.get_modules/{user_id}/{course_id}")
def user_getmodules(user_id,course_id):
    course = courses.search(where('id') == int(course_id))
    return(course[0])

#@app.get("/user.get_tasks/{user_id}/{module_id}")
#async def fetch_data():#id: int):
#    query = "SELECT * FROM events" # WHERE ID={}".format(str(id))
#    results = await database.fetch_all(query=query)
#
#    return  results
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
    print(course)
    # module id
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
    #print(mod['items'][0])
    #return(mod)

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
                                          }
            task_ids.append("'"+task.get('id')+"'")

    # select all most recent user-specific events

    #query = "SELECT * FROM events WHERE user_id=" + str(user_id) + " AND task_id IN (" + ','.join(task_ids) + ")"

    query = """SELECT * FROM events, (SELECT user_id, task_id, type, max(timestamp) as max_timestamp
    FROM events WHERE
    task_id IN (""" + ','.join(task_ids) + """) GROUP BY user_id, task_id, type) max_user WHERE
    events.user_id=max_user.user_id AND events.task_id = max_user.task_ID AND
    events.type = max_user.type AND events.timestamp = max_user.max_timestamp"""

    results = await database.fetch_all(query=query)

    query2 = """SELECT task_id, COUNT(*) AS count, max(timestamp) as max_timestamp FROM comments WHERE
    task_id IN (""" + ','.join(task_ids) + """) GROUP BY task_id;"""

    results_comments = await database.fetch_all(query=query2)
    print(results_comments)


    #    query2 = """SELECT max(timestamp) FROM events WHERE
    #task_id IN (""" + ','.join(task_ids) + """)"""

    #    results_timestamp = await database.fetch(query=query2)

    #return(results)
    import json
    #out=json.loads(res)
    #return(results)

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


    for i in range(len(mod['items'])):
        for j in range(len(mod['items'][i]['items'])):
            mod['items'][i]['items'][j]['stats']=stats_dic[mod['items'][i]['items'][j]['id']]

    return(mod)


def OLDuser_getmodules(user_id,module_id):
    course = courses.all()
    print(course)
    # module id
    # retrieve module
    mod = {}
    for c in course:
        if c.get('modules') is not None:
            for m in c.get('modules'):
                if m.get('id')==int(module_id):
                    mod = m
                    mod['course_id'] = c.get('id')
                    #return(m)
    # check for task completeness
    return(mod)

    for cat in mod.get('items'):
        for it in cat.get('items'):
            db.table('status').search(where('task_id')=='x1')[-1]

            stat = status.search(where('task_id')==it['id'])
            if len(stat)>0:
                stat=stat[-1]

    #else:
    #    return({})

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
