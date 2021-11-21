# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Flask, render_template, request, redirect, url_for
from .models import Module, Task, Course
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_

main = Blueprint('main', __name__)



@main.route('/')
def index():
    db.create_all()

    if current_user.is_authenticated:
         courses = Course.query.filter(Course.users.any(id=current_user.id)).all()
         #courses = Course.query.filter_by(User.id==current_user.id).all()
         return render_template('courses.html', courses=courses, name=current_user.name)
    else:
         return render_template("index.html")

@main.route('/modules/<course_id>')
@login_required
def get_modules(course_id):
    print(course_id)
    modules = Module.query.filter(Module.courses.any(id=course_id)).all()
    # modules = Module.query.filter(and_(Module.courses.any(id=course_id),
    #                               Module.users.any(id=current_user.id))).all()
    #modules=Module.query.filter().all() #any(id=course_id))).all()
    print(len(modules))
    return render_template("modules.html", modules = modules)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/todo')
@login_required
def todo():
    return render_template('todo.html', name=current_user.name)


@main.route('/courses2')
@login_required
def courses2():
    return render_template('courses2.html')

@main.route('/reset')
def reset_db():
    db.reflect()
    db.drop_all()

    db.create_all()

    from .models import User, Course, Courses_Users, Courses_Modules, Task, Module

    # Add fake users
    new_user = User(id=1,
                    email='hannes@datta-online.com',
                    name='Hannes Datta',
                    password=generate_password_hash('test', method='sha256'),
                    type = 'admin')
    # add the new user to the database
    db.session.add(new_user)

    # Add fake users
    new_user = User(id=2,
                    email='laura@datta-online.com',
                    name='Laura Datta',
                    password=generate_password_hash('test', method='sha256'),
                    type = 'student')
    # add the new user to the database
    db.session.add(new_user)

    # Add fake courses
    new_course = Course(id = 1,
                        name = 'Online Data Collection & Management',
                        description = "Learn to scrape the web!")
    db.session.add(new_course)

    new_course = Course(id = 2,
                        name = 'Data Preparation & Workflow Management',
                        description = "Professionalize working on empirical research projects!")
    db.session.add(new_course)

    new_course_membership = Courses_Users(course_id = 1,
                                           user_id = 2)
    db.session.add(new_course_membership)

    new_course_membership = Courses_Users(course_id = 2,
                                           user_id = 2)
    db.session.add(new_course_membership)


    # Add modules
    new_module = Module(id=1, name = 'Week 1')
    db.session.add(new_module)
    new_module = Module(id=2, name = 'Week 2')
    db.session.add(new_module)
    new_module = Module(id=3, name = 'Week 3')
    db.session.add(new_module)

    new_modules_courses = Courses_Modules(course_id=2, module_id = 1)
    db.session.add(new_modules_courses)

    new_modules_courses = Courses_Modules(course_id=2, module_id = 2)
    db.session.add(new_modules_courses)
    #new_modules_courses = Courses_Modules(course_id=2, module_id = 3)
    #db.session.add(new_modules_courses)

    db.session.commit()



    return('done')


# @main.route("/categories")
# def modules():
#     #category_list = Categories.query.all()
#     return render_template("profile.html", name=current_user.name, category_list=category_list)
#
# @main.route("/add_category", methods=["POST"])
# def add_category():#
#     title = request.form.get("title")
#     #new_todo = Categories(name=title,)
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("main.categories"))
