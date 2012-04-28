from flask import render_template,session,redirect,url_for

__author__ = 'Administrator'
from admin import app

@app.route('/')
def index():
    return render_template('index.html')