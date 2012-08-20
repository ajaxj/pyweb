from flask import Module,render_template
from flask.globals import request
from fkapp.models.greeting import User


__author__ = 'Administrator'


admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/index.html')

@admin.route("/users",methods=('GET','POST'))
def users():
    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        user = User(username=_username,password=_password)
        user.save()
        return render_template('admin/users.html')
    else:
        return render_template('admin/users.html')