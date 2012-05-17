#coding:utf-8
__author__ = 'window2003@gmail.com'
"""
后台管理的 view 模块
"""
from flask import  Module,render_template
#定义模块名称为admin
admin = Module(__name__)


@admin.route("/")
def index():
    return render_template("admin/index.html")

