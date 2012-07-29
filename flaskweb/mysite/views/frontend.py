# -*- coding:utf-8 -*-
from flask import Module,redirect,url_for,render_template,request,json,jsonify

__author__ = 'window2003@gmail.com'

frontend = Module(__name__)

@frontend.route('/')
def index():
    return render_template('index.html')


#***********************

@frontend.route('/bonetest')
def bonetest():
    return render_template('bone/bonetest.html')


#一个添加用户的例子
@frontend.route('/adduserdemo')
def adduserdemo():
    return render_template('bone/bone_adduser.html')

@frontend.route('/savefriend',methods=['GET','POST'])
def savefriend():
#    if request.method == 'POST':
#        data = json.loads(request.data);
#        print data['name']
#        return jsonify(success = True)
    return jsonify(success = False)
