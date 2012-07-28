# -*- coding:utf-8 -*-
__author__ = 'window2003@gmail.com'


from flask import Module,redirect,url_for

__author__ = 'window2003@gmail.com'

admin = Module(__name__)

@admin.route('/')
def index():
    return "this is admin"