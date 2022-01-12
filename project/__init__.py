# init.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import requests

# init SQLAlchemy so we can use it later in our models
# db = SQLAlchemy()

# /// = relative path, //// = absolute path

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config["SQLALCHEMY_ECHO"] = True

    app.config["API_URL"] = 'http://127.0.0.1'
    app.config["API_PORT"] = '8000'

    # db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #from .models import User
    from .main import AppUser

    @login_manager.user_loader
    def load_user(user_id):
        res=requests.get(app.config["API_URL"]+':' +app.config["API_PORT"] + '/user.info/' + str(user_id))
        ret=AppUser(res.json())
        #setattr(ret, 'is_authenticated', True)
        #print(res.json())
        return(ret)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
