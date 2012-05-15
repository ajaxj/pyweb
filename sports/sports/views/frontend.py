#coding:utf-8
"""
前端的控制器模块 view层
"""
__author__ = 'window2003@gmail.com'

from flask import Module,render_template

#定义模块名称
frontend = Module(__name__)

#首页的路由控制
@frontend.route("/")
def index():
    return render_template('home/index.html')
