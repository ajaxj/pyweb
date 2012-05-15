#coding=utf-8
"""
    应用的帮助模块
"""
__author__ = 'window2003@gmail.com'

from flask import current_app,g
from flaskext.themes import render_theme_template

def get_theme():
    return current_app.config['THEME']

def render_templates(template, **context):
    print template
    return render_theme_template(get_theme(), template, **context)