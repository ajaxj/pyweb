# -*- coding:utf-8
__author__ = 'window2003@gmail.com'

from flask import Module
from sports.extensions import db

link = Module(__name__)

@link.route("/")
def index(page = 1):
    return render_template("")

