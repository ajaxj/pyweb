from flask import Module,render_template,request,flash,redirect
from fkapp.models.greeting import User
from fkapp.forms import LoginForm

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


@admin.route("/login/", methods=("GET","POST"))
def login():
    form = LoginForm(username=request.args.get('username',None),next=request.args.get('next',None))
    if form.validate_on_submit():
        flash("Welcome back, %s"% form.username.data, "success")
        next_url = form.next.data
        print next_url
        print form.username.data
        print form.password.data
        print form.remember.data
        return redirect('signup')


    return render_template('admin/login.html',form = form)



def signup():
    form = 