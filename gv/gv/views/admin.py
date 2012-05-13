from flask import Module

__author__ = 'Administrator'


admin = Module(__name__)

@admin.route("/")
def index():
    print "this is admin"
    return "this is admin"
