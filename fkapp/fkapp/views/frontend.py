from flask import Module

__author__ = 'Administrator'


frontend = Module(__name__)

@frontend.route("/")
def index():
    print "this is home"
    return "this is home"