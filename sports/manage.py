#coding:utf-8
"""
应用的主控制
"""
from flaskext.script import Manager,Server, prompt_bool
from sports import create_app
from sports.extensions import db
#添加了模型引用就能直接使用create drop 这些方法
from sports.models.users import User
#from sports.models.blog import Post
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


if __name__ == "__main__":
    manager.run()

