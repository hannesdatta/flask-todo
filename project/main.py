# main.py

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user, login_user, logout_user, UserMixin
from flask import Flask, render_template, request, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_
from sqlalchemy.sql import text
import requests
from .emailtool import send_mail
from flask import Markup

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

         if current_user.created==current_user.changed:
            flash(Markup('Uhh... we picked a random nickname for you! Head over to your <a href="/me" class = "alert-link">settings</a> to change it!<br>You can make this message go away by changing your settings once...'))
            #flash(')

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
            flash('Boom! Check your email and use your magic login link!') #'<br>'+ link)
            send_mail(email, "Log in to *Pulse* now!", "Thanks for requesting your MAGIC LINK to log in back to *Pulse*. " + link)
        else:
            flash('Amazing that you join! CHeck your email now and use your magic link to log in!') #'<br>'+link)
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
    task_id = request.args.get('task_id')
    module_id = request.args.get('module_id')

    # retrieve stats for all tasks
    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.get_tasks/?user_id=' + str(current_user.id) + '&module_id=' + str(module_id)
    res=requests.get(url).json()
    task = {}

    # isolate current task
    for i in res.get('items'):
        for j in i.get('items'):
            if j.get('id')==task_id:
                task = j

    # pass some meta data to task object
    task['module_id']=res['id']
    task['module_name']=res['name']
    task['course_name']=res['course_name']
    task['course_id']=res['course_id']

    # load comments
    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/comments/show/?user_id=' + str(current_user.id) + '&task_id=' + str(task_id)
    comments=requests.get(url).json()

    comment_dic = []

    from datetime import datetime

    for comment in comments:
        res=comment
        ts_date=datetime.utcfromtimestamp(res['timestamp']).strftime('%d-%m-%Y')
        ts_time=datetime.utcfromtimestamp(res['timestamp']).strftime('%H:%M')

        res['timestamp_printable'] = ts_date + ' at ' + ts_time
        if (datetime.utcnow().strftime('%d-%m-%Y'))==ts_date: res['timestamp_printable'] = 'Today at ' + ts_time
        if str(int((datetime.utcnow().strftime('%d')))-1)+(datetime.utcnow().strftime('-%m-%Y'))==ts_date: res['timestamp_printable'] = 'Yesterday at ' + ts_time
        res['show_delete'] = res['user_id']==current_user.id

        url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.info/' + str(res['user_id'])
        nickname=requests.get(url).json()['nickname']
        res['nickname'] = nickname
        comment_dic.append(res)
    #    return redirect(request.referrer)
    #session['url'] = url_for('comments')

    return render_template('comments.html', task=task, comments=comment_dic)


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

@main.route('/me')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,
    user=current_user)

@main.route('/todo/<module_id>')
@login_required
def todo(module_id):
    url=current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.get_tasks/?user_id=' + str(current_user.id) + '&module_id=' + str(module_id)
    res=requests.get(url).json()
    print(url)
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

    return redirect(request.referrer)
    #return redirect(url_for("main.todo", module_id=module))


@main.route('/delete_comment/')
@login_required
def del_message():
    comment_id = request.args.get('comment_id')
    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/comments/delete/?comment_id=' + comment_id
    print(url)

    res = requests.get(url)
    #print(res.text)
    return redirect(request.referrer)


@main.route('/gif/')
@login_required
def show_gifs():

    gifs = ['https://giphy.com/gifs/thumbs-up-elon-musk-OxrQAuM5kKMKHn14ls',
    'https://giphy.com/gifs/americasgottalent-thumbs-up-agt-simon-cowell-3o72FcJmLzIdYJdmDe']

    import random

    random.choice(gif)

    #w/ 20% chance of getting a gif

    # extract everything after last -

    #<iframe src="https://giphy.com/embed/BgWGTu2TgdP44" width="480" height="270" frameBorder="0"


    #class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dance-rap-rave-BgWGTu2TgdP44">via GIPHY</a></p>

@main.route('/submit_comment/', methods=['POST'])
@login_required
def submit_message():

    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/comment'
    import json
    requests.post(url, data = json.dumps({'text':request.form.get('comment'),
                                         'user_id': current_user.id,
                                         'task_id': request.args.get('task_id')
                                         }))

    return redirect(request.referrer)

@main.route('/saveuser/', methods=['POST'])
@login_required
def saveuser():

    url = current_app.config["API_URL"]+':' +current_app.config["API_PORT"] + '/user.setinfo'
    import json
    requests.post(url, data = json.dumps({'nickname':request.form.get('nickname'),
                                         'user_id': current_user.id
                                         }))

    return redirect(request.referrer)
