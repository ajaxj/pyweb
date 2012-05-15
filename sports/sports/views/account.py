# -*- coding:utf-8


__author__ = 'Administrator'
from flask import Module,request,redirect,flash,render_template

from sports.extensions import db
from sports.models.users import User,UserCode
from sports.forms import LoginForm,SignupForm
#from sports.helpers import render_templates

account = Module(__name__)

@account.route("/login/", methods=("GET","POST"))
def login():
    form = LoginForm(login=request.args.get('login',None),
        next=request.args.get('next',None))
    if form.validate_on_submit():
        flash("Welcome back, %s"% form.login.data, "success")
        next_url = form.next.data
        print next_url
#        print "this is submit"
#        print form.login.data
#        print form.password.data
#        return redirect('signup')

    return render_template("account/login.html",form=form)

@account.route("/signup/",methods=("GET","POST"))
def signup():
    form = SignupForm(next=request.args.get('next',None))
    if form.validate_on_submit():
        # 注册码
        code =  UserCode.query.filter_by(code=form.code.data).first()
        if code:
            user = User(role=code.role)
            form.populate_obj(user)
            #db.session.add(user)
            #db.session.commit()
            flash("Welcome, %s" % user.nickname, "success")
            next_url = form.next.data
            print next_url
        else:
            form.code.errors.append("Code is not allowed")

   # TODO 如果使用themes扩展，使用下面的theme方法，不用写目录，但与flask8支持不好
   #唯一的好处就是能在config里面写目录配置
   # #extends theme("layout.html")
   # return render_templates("account/signup.html", form=form)
    return render_template("account/signup.html",form=form)
