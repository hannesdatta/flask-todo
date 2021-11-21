# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Flask, render_template, request, redirect, url_for
from .models import Categories, Todo
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    db.create_all()

    if current_user.is_authenticated:
         return render_template('courses.html', name=current_user.name)
    else:
         return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/todo')
@login_required
def todo():
    return render_template('todo.html', name=current_user.name)


@main.route('/courses')
@login_required
def courses():
    return render_template('courses.html')


@main.route("/categories")
def categories():
    category_list = Categories.query.all()
    return render_template("profile.html", name=current_user.name, category_list=category_list)

@main.route("/add_category", methods=["POST"])
def add_category():#
    title = request.form.get("title")
    new_todo = Categories(name=title,)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.categories"))
