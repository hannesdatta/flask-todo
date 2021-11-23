# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Flask, render_template, request, redirect, url_for
from .models import Module, Task, Course, Modules_Tasks, Checked
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_
from sqlalchemy.sql import text

main = Blueprint('main', __name__)



@main.route('/')
def index():
    db.create_all()

    if current_user.is_authenticated:
         courses = Course.query.filter(Course.users.any(id=current_user.id)).all()
         #courses = Course.query.filter_by(User.id==current_user.id).all()
         return render_template('courses.html', courses=courses, user=current_user)
    else:
         return render_template("index.html")

@main.route('/modules/<course_id>')
@login_required
def get_modules(course_id):
    modules = Course.query.filter(Course.id==course_id).filter(Course.users.any(id=current_user.id)).first().modules
    course = Course.query.filter(Course.id==course_id).first()
#
#     rs = db.session.query(User).from_statement(
# ...  text("SELECT * FROM users where name=:name")).params(name='ed').a
#
#     rs = db.session.execute('SELECT * FROM modules m, courses_modules cm, courses_users cu WHERE m.id = cm.module_id AND cm.course_id = cu.course_id AND cu.user_id = ' + str(current_user.id))

    return render_template("modules.html", modules = modules, course = course)

@main.route('/updatepage')
def updatepage():
    return render_template('update.html', name=current_user.name)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/todo/<module_id>')
@login_required
def todo(module_id):

    module = Module.query.filter(Module.id==module_id).first()

    course = Course.query.filter(Course.modules.any(id=module_id)).first()

    tasks = db.session.query(Task, Checked).filter(Task.modules.any(id=module_id)).join(Checked, Checked.task_id == Task.id, isouter=True).filter(
                     or_(
                         Checked.user_id.in_([current_user.id]),
                         Checked.user_id == None
                     )).all()

    return render_template('todo.html', tasks=tasks, module=module, course = course)

@main.route("/todo-update/<int:module_id>/<int:todo_id>")
@login_required
def update_task(module_id, todo_id):
    # check whether task checked exists in database
    task_check = Checked.query.filter(and_(Checked.user_id==current_user.id,
                                           Checked.module_id == module_id,
                                           Checked.task_id == todo_id))

    # task does not yet exist in checked table
    count = task_check.count()
    if (count==0):
        new_update = Checked(user_id=current_user.id, module_id=module_id, task_id = todo_id, complete = 1)
        db.session.add(new_update)
        db.session.commit()

    if (count==1):
        task_check.first().complete = not task_check.first().complete
        db.session.commit()

    return redirect(url_for("main.todo", module_id=module_id))


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
                    nickname = "Laura",
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

    new_modules_courses = Courses_Modules(course_id=1, module_id = 3)
    db.session.add(new_modules_courses)


    # Tasks
    new_task = Task(id=1, name = 'Task 1', description = 'blabla')
    db.session.add(new_task)
    new_task = Task(id=2, name = 'Task 1b', description = 'blabla')
    db.session.add(new_task)
    new_task = Task(id=3, name = 'Task 1c', description = 'blabla')
    db.session.add(new_task)
    new_task = Task(id=4, name = 'Task 1d', description = 'blabla')
    db.session.add(new_task)
    new_task = Task(id=5, name = 'Task 1e', description = 'blabla')
    db.session.add(new_task)

    new_modules_tasks = Modules_Tasks(module_id=2,task_id=1)
    db.session.add(new_modules_tasks)
    new_modules_tasks = Modules_Tasks(module_id=2,task_id=2)
    db.session.add(new_modules_tasks)
    new_modules_tasks = Modules_Tasks(module_id=2,task_id=3)
    db.session.add(new_modules_tasks)


    #new_modules_courses = Courses_Modules(course_id=2, module_id = 3)
    #db.session.add(new_modules_courses)

    new_checked = Checked(user_id=2, module_id=2, task_id = 1,complete = True)
    db.session.add(new_checked)


    db.session.commit()

    return('done')
