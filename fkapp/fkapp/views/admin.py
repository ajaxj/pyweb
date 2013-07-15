# -*- coding:utf-8 -*-
from flask import Module,render_template,request,flash,redirect

# from fkapp.forms import LoginForm
from fkapp.models.model import Admin,Hakuzy


__author__ = 'Administrator'


admin = Module(__name__)

#首页
@admin.route("/")
def index():
    return render_template('admin/index.html')


#管理员列表
@admin.route('/admins')
def admins():
    _admins = Admin.query.all()
    return render_template('admin/admins.html',admins = _admins)


@admin.route('/hakuzylist')
def hakuzylist():
    _hakuzylist  = Hakuzy.query.limit(10).all()
    return render_template('admin/hakuzylist.html',hakuzylist=_hakuzylist)



@admin.route('/users')
def users():
    return redirect('/')


@admin.route('/login')
def login():
    return redirect('/')



#
# @admin.route("/users",methods=('GET','POST'))
# def users():
#     if request.method == 'POST':
#         _username = request.form['username']
#         _password = request.form['password']
#         user = User(username=_username,password=_password)
#         user.save()
#         return render_template('admin/users.html')
#     else:
#         return render_template('admin/users.html')
#
#
# @admin.route("/login/", methods=("GET","POST"))
# def login():
#     form = LoginForm(username=request.args.get('username',None),next=request.args.get('next',None))
#     if form.validate_on_submit():
#         flash("Welcome back, %s"% form.username.data, "success")
#         next_url = form.next.data
#         print next_url
#         print form.username.data
#         print form.password.data
#         print form.remember.data
#         return redirect('signup')
#
#
#     return render_template('admin/login.html',form = form)
#
#
#
# def signup():
#     form =