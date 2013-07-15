# -*- coding:utf-8 -*-
from flask import render_template,session,redirect,url_for,g
from admin.models.model import Admin, User
from admin import app, db






@app.route('/')
def index():
    # admin = Admin("admin","1234")
    # db.session.add(admin)
    # db.session.commit()
    # user = User(email="email1")
    # db.session.add(user)
    # db.session.commit()
    # users = User.query.all()
    # print len(users)
    return render_template('index.html')


@app.route('/users')
def users():
    _users = User.query.all()
    return render_template('users.html',users=_users)


@app.route('/admins')
def admins():
    return render_template('admins.html')

@app.route('/login')
def login():
    return render_template('login.html')