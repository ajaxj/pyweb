# -*- coding:utf-8
from flask.ext.script import Manager,Server
from fkapp import create_app
from fkapp.extensions import db
__author__ = 'window2003@gmail.com'

#建立脚本管理，并且建立一个应用，并且引用配置
manager = Manager(create_app('config.cfg'))
manager.add_command("runserver",Server())
# 服务器上面改成下面
#manager.add_command("runserver",Server('0.0.0.0',port=5000))

@manager.command
def createall():
    db.create_all()

@manager.command
def dropall():
    db.drop_all()



if __name__ == "__main__":
    manager.run()
