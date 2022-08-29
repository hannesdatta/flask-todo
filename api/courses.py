from tinydb import TinyDB, Query
from flask_login import UserMixin
from datetime import datetime

f = open("odcm.json", "r")
con = f.read()

courses = [json.loads(con)]

leaderboard = [
    {
    "id": "daily_activity",
    "order": 1,
    "task_short_name":"Daily Activity",
    "task_description":"Earn XP by logging in every day!",
    "badge":"",
    "xp_earned":50,
    "type_of_task":"achievement"},
    {
    "id": "complete_to_do",
    "order": 2,
    "task_short_name":"Complete a to-do",
    "task_description":"Mark a to-do as complete",
    "badge":"",
    "xp_earned":30,
    "type_of_task":"achievement"},
    {
    "id": "complete_to_do_top3",
    "order": 3,
    "task_short_name":"Top 3 completing a to-do",
    "task_description":"Be part of the first 3 to finish a certain to-do",
    "badge":"",
    "xp_earned":30,
    "type_of_task":"achievement"},
    {
    "id": "complete_to_do_top10",
    "order": 4,
    "task_short_name":"Top 10 completing a to-do",
    "task_description":"Be part of the first 10 (but not first 3) to finish a certain to-do",
    "badge":"",
    "xp_earned":15,
    "type_of_task":"achievement"},
    {
    "id": "complete_module",
    "order":5,
    "task_short_name":"Complete all to-dos from a given week",
    "task_description":"Complete all to-dos from a given week",
    "badge":"",
    "xp_earned":50,
    "type_of_task":"achievement"},
    {
    "id": "complete_module_top3",
    "order": 6,
    "task_short_name":"Top 3 completing all to-dos from a given week",
    "task_description":"Be part of the first 3 to finish all to-dos within a given week",
    "badge":"U+26A1",
    "xp_earned":100,
    "type_of_task":"achievement"},
    {
    "id": "complete_module_top10",
    "order": 7,
    "task_short_name":"Top 10 completing all to-dos from a given week",
    "task_description":"Be part of the first 10 (but not first 10) to finish all to-dos within a given week",
    "badge":"",
    "xp_earned":50,
    "type_of_task":"achievement"},
    {
    "id": "help_others",
    "order": 8,
    "task_short_name":"Mark a to-do with 'can help others'",
    "task_description":"Learning-by-teaching is proven to to boost knowledge retention and understanding. Therefore, marking tasks with 'can help others' will not only be beneficial to others, but to you as well!",
    "badge":"",
    "xp_earned":10,
    "type_of_task":"help"},
    {
    "id": "write_comment",
    "order": 9,
    "task_short_name":"Write a comment on a to-do",
    "task_description":"To stimulate engagement and participation, leaving a comment will give you additional XP!",
    "badge":"",
    "xp_earned":20,
    "type_of_task":"comment"}]

db = TinyDB('db.json')

#db.drop_tables()
db.drop_table('courses')
table = db.table('courses')
#users = db.table('users')

print('inserting new courses')
table.insert(course_odcm)

print('done inserting')

try:
    db.drop_table('achievements')
except:
    1+1

achievements = db.table('achievements')
for a in leaderboard: achievements.insert(a)

class AppUser(UserMixin, object):

    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def get_id(self):
        return(self.id)
