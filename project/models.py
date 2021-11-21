# models.py

from flask_login import UserMixin
from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Courses_Users(db.Model):
    __tablename__ = 'courses_users'
    course_id = db.Column(ForeignKey('courses.id'), primary_key=True)
    user_id = db.Column(ForeignKey('users.id'), primary_key=True)
    extra_data = Column(db.String(50))
    #endDate = Column(db.Date)

class Modules_Tasks(db.Model):
    __tablename__ = 'modules_tasks'
    module_id = db.Column(ForeignKey('modules.id'), primary_key=True)
    task_id = db.Column(ForeignKey('tasks.id'), primary_key=True)
    #extra_data = Column(db.String(50))
    #endDate = Column(db.Date)

class Courses_Modules(db.Model):
    __tablename__ = 'courses_modules'
    course_id = db.Column(ForeignKey('courses.id'), primary_key=True)
    module_id = db.Column(ForeignKey('modules.id'), primary_key=True)
    #extra_data = Column(db.String(50))
    #endDate = Column(db.Date)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    type = db.Column(db.String(10))
    courses = relationship("Course", secondary = 'courses_users', back_populates = "users")


class Module(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    tasks = relationship("Task", secondary = 'modules_tasks', back_populates="modules")
    courses = relationship("Course", secondary = 'courses_modules', back_populates="modules")

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    modules = relationship("Module", secondary = 'modules_tasks', back_populates = "tasks")

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    users = relationship("User", secondary = 'courses_users', back_populates="courses")
    modules = relationship("Module", secondary = 'courses_modules', back_populates="courses")

# class Module(db.Model):
#     __tablename__ = 'modules'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     description = db.Column(db.String(100))
#     tasks = relationship("User", secondary = 'courses_users', back_populates="courses")


#
# class ItemDetail(Base):
#     __tablename__ = 'ItemDetail'
#     id = Column(Integer, primary_key=True, index=True)
#     itemId = Column(Integer, ForeignKey('Item.id'))
#     detailId = Column(Integer, ForeignKey('Detail.id'))
#     endDate = Column(Date)
#
# class Item(Base):
#     __tablename__ = 'Item'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     description = Column(Text)
#     details = relationship('Detail', secondary=ItemDetail, backref='Item')
#
# class Detail(Base):
#     __tablename__ = 'Detail'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     value = Column(String)
#     items = relationship('Item', secondary=ItemDetail, backref='Detail')
