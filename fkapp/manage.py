# -*- coding:utf-8
from flaskext.script import Manager
from fkapp import create_app
__author__ = 'window2003@gmail.com'

#建立脚本管理，并且建立一个应用，并且引用配置
manager = Manager(create_app('config.cfg'))



if __name__ == "__main__":
    manager.run()
