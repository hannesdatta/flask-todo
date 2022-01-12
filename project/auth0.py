# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db
from random import random
import math
from datetime import datetime, timedelta
from .emailtool import send_mail

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('authentication.html')

@auth.route('/start/<email>/<token>')
def start(email, token):
    user = User.query.filter_by(email=email).first()

    remember = True #if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    now = datetime.utcnow()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, token):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.signup')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.machines'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    now = datetime.utcnow()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, token) or not user.expiry<=now:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.signup')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))
    #return redirect(url_for('main.courses'))

@auth.route('/signup')
def signup():
    return render_template('login.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    #name = request.form.get('name')
    #password = request.form.get('password')

    # check if user is authorized:
    if (email in ['h.datta@tilburguniversity.edu', "hannes@datta-online.com"]):

        # check whether user exist
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        token = str(math.ceil(random()*1E6))+'researchcloud'
        print(token)
        now = datetime.utcnow()
        expiry = now+ timedelta(minutes=15)
        if user: # if a user is found, update login token
            user.expiry = expiry
            user.password = generate_password_hash(token, method='sha256')
            db.session.commit()
            link = request.url_root + 'start/'+user.email+'/'+token

            send_mail(user.email, "Log in to *Pulse* now!", "Thanks for requesting your MAGIC LINK to log in back to *Pulse*. " + link)

            flash('Thanks for being back. An email has been sent w/ your login link!')

        if not user: # create
            new_user = User(email=email, password=generate_password_hash(token, method='sha256'),
            expiry = expiry)

            db.session.add(new_user)
            db.session.commit()
            link = request.url_root + 'start/'+email+'/'+token

            send_mail(email, "Welcome to Pulse!", "Thanks for using PULSE, Tilburg's tool to help you keep on track with your course work. Please use this MAGIC LINK to login now: " + link)

            flash('An email has been sent w/ your login link! Check your inbox now!')

        return redirect(url_for('auth.signup'))

    flash('Not authorized. Think this is a mistake? Email h.datta@tilburguniversity.edu!')

    #if user: # if a user is found, we want to redirect back to signup page so user can try again
    #    flash('Email address already exists')
    #    return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    #new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database

    return redirect(url_for('auth.signup'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
