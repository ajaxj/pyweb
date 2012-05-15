#coding:utf-8
"""
应用的主控制
"""
import uuid

from flask import Flask, current_app
from flaskext.script import Server, Shell, Manager, Command, prompt_bool

from sports import create_app
from sports.extensions import db

#添加了模型引用就能直接使用create drop 这些方法
from sports.models.users import User,UserCode
__author__ = 'window2003@gmail.com'


manager = Manager(create_app('config.cfg'))
manager.add_command("runserver",Server())



@manager.command
def createall():
    """建立数据表"""
    db.create_all()
    manager.app.logger.debug("create all database")

@manager.command
def dropall():
    """删除所有的表"""
    if prompt_bool("Are you sure? you will lost all your data"):
        db.drop_all()
        manager.app.logger.debug("drop all database")



#初始添加数据的方法
@manager.option('-r','--role',dest='role',default='member')
@manager.option('-n','--number',dest='number',default=1,type=int)
def createcode(role,number):
    codes = []
    usercodes = []
    for i in range(number):
        code = unicode(uuid.uuid4()).split("-")[0]
        codes.append(code)
        usercode = UserCode()
        usercode.code = code
        if role == 'admin':
            usercode.role = User.ADMIN
        elif role == "moderator":
            usercode.role = User.MODERATOR
        else:
            usercode.role = User.MEMBER
        usercodes.append(usercode)
    if number == 1:
        db.session.add(usercode)
    else:
        db.session.add_all(usercodes)
    db.session.commit()
    print "Sign up code:"
    for i in codes:
        print i
    return

if __name__ == "__main__":
    # createall
    # dropall
    # runserver
    # createcode  -r admin
    # createcode -r member -n 3
    manager.run()

