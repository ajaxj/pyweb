from flask import render_template,session,redirect,url_for

__author__ = 'Administrator'
from admin import app

@app.route('/')
def index():
    return render_template('index.html')



def users():
    return render_template('users')


@app.route('/login')
def login():
    return render_template('login.html')