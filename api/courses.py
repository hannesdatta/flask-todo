from tinydb import TinyDB, Query
from flask_login import UserMixin
from datetime import datetime

course ={
  "name": "Online Data Collection and Management",
  "description": "Learn how to scrape the web!",
  "id": 1,
  "users": [],
  "modules": [
    {
      "name": "Week 1",
      "description": "Get started installing your computer!",
      "id": 1,
      "order": 1,
      "deadline": "2022-01-31",
      "items": [
        {"category_name": "Category",
         "id": 1,
         "description": "This is a category",
         "items" : [
            {
              "name": "task 1",
              "id": "x1",
              "description": "bla"
            },
            {
              "name": "task 2",
              "id": "x2",
              "description": "blu"
            },
            {
              "name": "task 3",
              "id": "x3",
              "description": "tra"
            }
            ]
     },
     {"category_name": "Category 2",
      "id": 2,
      "description": "This is a category 2",
      "items" : [
         {
           "name": "task 1b",
           "id": "x4",
           "description": "bla"
         },
         {
           "name": "task 2b",
           "id": "x5",
           "description": "blu"
         },
         {
           "name": "task 3b",
           "id": "x6",
           "description": "tra"
         }
         ]
  }
   ]
  },
  {
    "name": "Week 2",
    "description": "Let's start to scrape!",
    "id": 2,
    "order": 1,
    "deadline": "2022-01-31",
    "items": [
      {"category_name": "Category",
       "id": 1,
       "description": "This is a category",
       "items" : [
          {
            "name": "task 1",
            "id": "1",
            "description": "bla"
          },
          {
            "name": "task 2",
            "id": "2",
            "description": "blu"
          },
          {
            "name": "task 3",
            "id": "3",
            "description": "tra"
          }
          ],
         "modules": []
   }
 ]
}
]
 }

course2 ={
  "name": "Data Preparation & Workflow Management",
  "description": "Manage your research projects efficiently!",
  "id": 3,
  "users": []}


db = TinyDB('db.json')
db.drop_tables()
table = db.table('courses')
users = db.table('users')
status = db.table('status')

table.insert(course)
table.insert(course2)

users.insert({'email': 'h.datta@tilburguniversity.edu',
              'name': 'Hannes Datta',
              'nickname': 'Haynce',
              'id': 1})

status.insert({'user_id': 1,
               'task_id': 'x1',
               'completed': True,
               'has_question': True,
               'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
})

status.insert({'user_id': 1,
               'task_id': 'x1',
               'completed': True,
               'has_question': False,
               'timestamp': datetime.utcnow().strftime('%Y-%m-10 %H:%M:%S')
})


class AppUser(UserMixin, object):

    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def get_id(self):
        return(self.id)


my_dict = {"Name": "Geeks",
           "Rank": "1223",
           "Subject": "Python",
           "email": "h@d.com",
           "id": 1}
my_dict2 = {"Name": "Geeks",
           "Rank": "1223",
           "Subject": "Python",
           "email": "h@d.com",
           "id": 2}

result = AppUser(my_dict2)

# printing the result
print("After Converting Dictionary to Class : ")
#print(result.Name, result.Rank, result.Subject)
print(type(result))
print(result.get_id())
#result.is_authenticated=False
print(result.is_authenticated)
