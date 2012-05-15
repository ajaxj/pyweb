# -*- coding:utf-8

__author__ = 'Administrator'
from flask import Module,request,render_template,redirect

from sports.forms import LoginForm,SignupForm


account = Module(__name__)

@account.route("/login/", methods=("GET","POST"))
def login():
    print "this is login"
    form = LoginForm()
    #form = LoginForm(login=request.args.get('login',None),next=request.args.get('next',None))
    if form.submit():
        print "this is submit"
        print form.login.data
        print form.password.data
        return redirect('signup')

    return render_template("account/login.html",form=form)

@account.route("/signup/",methods=("GET","POST"))
def signup():
    form = SignupForm(next=request.args.get('next',None))
    if form.validate_on_submit():
        code =  UserCode.query.filter_by()
    return render_template("account/signup.html",form=form)
