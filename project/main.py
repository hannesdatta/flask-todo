# main.py

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user, login_user, logout_user, UserMixin
from flask import Flask, render_template, request, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_
from sqlalchemy.sql import text
import requests
from .emailtool import send_mail

main = Blueprint('main', __name__)


@main.route('/')
def index():
    #db.create_all()

    if current_user.is_authenticated:
         #courses = Course.query.filter(Course.users.any(id=current_user.id)).all()
         res=requests.get(current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.get_courses/' + str(current_user.id))
         courses=res.json()
         course_list=[]
         for c in courses:
             c['has_modules'] = False
             try:
                 len(c.get('modules'))>0
                 c['has_modules'] = True
             except:
                 1
             course_list.append(c)
         #
         #courses = Course.query.filter_by(User.id==current_user.id).all()
         return render_template('courses.html', courses=course_list, user=current_user)
    else:
         return render_template("index.html")

@main.route('/old', methods=['POST'])
def old_login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.index')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))
    #return redirect(url_for('main.courses'))

@main.route('/', methods=['POST'])
def main_login_post():
    email = request.form.get('email')
    #if request.form.get('remember') remember = 'True' else remember = 'False'

    # get users from APIs
    import re
    regex = r'[@]tilburguniversity[.]edu$|[@]datta[-]online[.]com$'

    # is user authorized to use service?
    if len(re.findall(regex, email))<1:
        flash('So sorry... you need to use an @tilburguniversity.edu address to get started! Want to try again?')
        return redirect(url_for('main.index'))

    res=requests.get(current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.gettoken/?email=' + email)#+'&remember='+remember)

    if (res.json().get('success')=='True'):
        link = request.url_root + 'launch/'+res.json()['token']

        if (res.json().get('new')=='False'):
            flash('Boom! Check your email and use your magic login link!<br>'+ link)
            send_mail(email, "Log in to *Pulse* now!", "Thanks for requesting your MAGIC LINK to log in back to *Pulse*. " + link)
        else:
            flash('Amazing that you join! CHeck your email now and use your magic link to log in!<br>'+link)
            send_mail(email, "Welcome to Pulse!", "Thanks for using PULSE, Tilburg's tool to help you keep on track with your course work. Please use this MAGIC LINK to login now: " + link)
    return redirect(url_for('main.index'))

class AppUser(UserMixin, object):

    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def get_id(self):
        return(self.id)


@main.route('/launch/<token>')
def launch(token):
    # verify token exists and user can log in

    res=requests.get(current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.checktoken/' + token)
    #print(res.json())
    user = AppUser(res.json())

    remember = True

    if not user.success==True:
            flash('Uhm... your magic link didn\'t work. Try getting another one!')
            return redirect(url_for('main.index')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    #user.is_authenticated = True
    void=login_user(user, remember=remember)
    #print(void)
    #print(user.is_authenticated)
    return redirect(url_for('main.index'))


@main.route('/comments')
@login_required
def get_comments():
    #modules = Course.query.filter(Course.id==course_id).filter(Course.users.any(id=current_user.id)).first().modules
    #course = Course.query.filter(Course.id==course_id).first()
#
#     rs = db.session.query(User).from_statement(
# ...  text("SELECT * FROM users where name=:name")).params(name='ed').a
#
#     rs = db.session.execute('SELECT * FROM modules m, courses_modules cm, courses_users cu WHERE m.id = cm.module_id AND cm.course_id = cu.course_id AND cu.user_id = ' + str(current_user.id))

    return render_template("comments.html")


@main.route('/modules/<course_id>')
@login_required
def get_modules(course_id):

    res=requests.get(current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.get_modules/' + str(current_user.id) + '/' + str(course_id))
    modules = res.json().get('modules')
    course = res.json()

    #modules = Course.query.filter(Course.id==course_id).filter(Course.users.any(id=current_user.id)).first().modules
    #course = Course.query.filter(Course.id==course_id).first()
    return render_template("modules.html", modules = modules, course = course)

@main.route('/updatepage')
def updatepage():
    return render_template('update.html', name=current_user.name)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,
    user=current_user)

@main.route('/todo/<module_id>')
@login_required
def todo(module_id):

    res=requests.get(current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.get_tasks/?user_id=' + str(current_user.id) + '&module_id=' + str(module_id)).json()
    print(res)
    return render_template('todo.html', tasks=res)

@main.route("/todo-update/")
@login_required
def update_task():
    task_id = request.args.get('task_id')
    type = request.args.get('type')
    status = request.args.get('status')
    module = request.args.get('module')

    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.set_tasks/?user_id=' + str(current_user.id) + '&task_id=' + str(task_id)+ '&type=' + str(type)+ '&status=' + str(status)
    print(url)
    res=requests.get(url).json()
    #print(res)


    return redirect(url_for("main.todo", module_id=module))
