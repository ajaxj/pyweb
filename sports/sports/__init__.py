#coding=utf-8
"""
    应用的建立，建立在__init__里，便于引用
"""


__author__ = 'window2003@gmail.com'
import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask,request
from sports.extensions import db

#from flaskext.babel import Babel, gettext as _
from flaskext.themes import setup_themes
from flaskext.principal import Principal
from sports import views,helpers
from sports.helpers import render_templates

#默认的flask应用名称
DEFAULT_APP_NAME = "sports"
#所有模块路由分配的dict
DEFAULT_MODULES = (
    (views.frontend,""),    #模块包名，url前缀
    (views.admin,"/admin"),
    (views.account, "/account"),
)

#config 配置文件名 modules 一个模块的列表
# return app 对象
def create_app(config=None, modules=None):
    #如果模块列表为空，就使用上面定义了的默认的
    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)
    #读取config
    app.config.from_pyfile(config)
    #初始扩展模块
    configure_extensions(app)


    # TODO 各种配置
    #配置log
    configure_logging(app)


    #注册模块，用列表实现批量注册

    #configure_i18n(app)
    configure_modules(app,modules)

    return app



#扩展配置
def configure_extensions(app):
    #SQLAlchemy 装载 这个app的config并且初始数据库
    db.init_app(app)
    setup_themes(app)
    # todo 还有别的扩展


def configure_identity(app):
    principal = Principal(app)




#多语言
def configure_i18n(app):

    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        accept_languages = app.config.get('ACCEPT_LANGUAGES',['en','zh'])
        return request.accept_languages.best_match(accept_languages)



def configure_modules(app,modules):
    for module,url_prefix in modules:
        app.register_module(module,url_prefix=url_prefix)

#给应用添加log
def configure_logging(app):
    #mail handler
    # log 打印的样式
    formatter = logging.Formatter( '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    #添加一个debug log文件的主式
    #得到log的文件名,通过整合
    debug_log = os.path.join(app.root_path,app.config['DEBUG_LOG'])
    #定义连续log文件写入
    debug_file_handler = RotatingFileHandler(debug_log,maxBytes=100000,backupCount=10)
    #log level定义
    debug_file_handler.setLevel(logging.DEBUG)
    #log 格式定义
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)