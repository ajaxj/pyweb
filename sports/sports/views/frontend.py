#coding:utf-8
"""
前端的控制器模块 view层
"""
__author__ = 'window2003@gmail.com'

from flask import Module,render_template

#定义模块名称
frontend = Module(__name__)

#首页的路由控制,和一些默认的参数
@frontend.route("/")
def index(year=None,month=None,day=None,page=1):
    if page<1:page=1
    #page_obj = Post.query.
    return render_template('home/index.html')
