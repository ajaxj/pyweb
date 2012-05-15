from flaskext.wtf import Form,TextField,HiddenField,BooleanField,PasswordField,SubmitField,ValidationError,required,\
    email,equal_to,regexp

#from flaskext.babel import gettext, lazy_gettext as _
__author__ = 'window2003@gmail.com'

class LoginForm(Form):
    login = TextField("Username or email address")
    password = PasswordField("Password")
    remember = BooleanField("Remember me")
    next = HiddenField()
    submit = SubmitField("Login")

class SignupForm(Form):
    username = TextField("Username",validators=[required(message=("Username required"))])
    nickname = TextField("Nickname",validators=[required(message=("Nickname required"))])
    password = PasswordField("Password",validators=[required(message=("Password required"))])
    password_again = PasswordField("Password again",validators=[equal_to("password",message=("password don't match"))])
    email = TextField("Email address",validators=[required(message=("Email address required"))])
    code = TextField("Signup Code")
    next = HiddenField()
    submit = SubmitField("Signup")
