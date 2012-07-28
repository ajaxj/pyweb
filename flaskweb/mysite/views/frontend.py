# -*- coding:utf-8 -*-
from flask import Module,redirect,url_for

__author__ = 'window2003@gmail.com'

frontend = Module(__name__)

@frontend.route('/')
def index():
    return "this is home"