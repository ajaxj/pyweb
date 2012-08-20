import datetime
from flask import Module,render_template
from fkapp.models.greeting import Greeting

__author__ = 'Administrator'


frontend = Module(__name__)

@frontend.route("/")
def index():
    greet = Greeting(
        author="Benoit1111",
        content="Welcome to couchdbkit world",
        date=datetime.datetime.utcnow()
    )
    greet.save()
    return render_template('index.html')