# models.py

from flask_login import UserMixin
from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    category = db.Column(db.Integer, primary_key = False)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    children = relationship("Association")

class Association(db.Model):
    __tablename__ = 'courses_users'
    left_id = db.Column(ForeignKey('courses.id'), primary_key=True)
    right_id = db.Column(ForeignKey('user.id'), primary_key=True)
    extra_data = db.Column(db.String(50))
    child = relationship("User")
