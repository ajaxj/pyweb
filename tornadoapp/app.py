# -*- coding:utf-8
import os
import logging
import tornado.auth
import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# TODO A

# 定义配置变量
from tornado.options import define,options
define("port",default=8888,help="run on the given port",type=int)
define("mysql_host",default="127.0.0.1:3306",help="database host")
define('mysql_database',default="ajaxj",help="database name")
define('mysql_user',default="root",help="database user")
define('mysql_password',default="",help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",HomeHandler),
            (r"/entry/([^/]+)",EntryHandler),
            (r"/compose",ComposeHandler),
        ]
        settings = dict(
            app_title = u"tornade app",
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            debug = True,
            #log_to_stderr = True,
            # TODO A
        )
        tornado.web.Application.__init__(self,handlers,**settings)
        #定义一个公共的db对象
        self.db = tornado.database.Connection(host=options.mysql_host,database=options.mysql_database,user=options.mysql_user,password=options.mysql_password)

#控制器超类
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db



#首页
class HomeHandler(BaseHandler):
    def get(self):
        entries = self.db.query("SELECT * FROM entries ORDER BY published "
                                "DESC LIMIT 5")
        if not entries:
            self.redirect("/compose")
            return
        self.render("home.html", entries=entries)


class EntryHandler(BaseHandler):
    def get(self, slug):
        entry = self.db.get("SELECT * FROM entries WHERE slug = %s", slug)
        if not entry: raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)

class ComposeHandler(BaseHandler):
    def get(self):
        id = self.get_argument("id",None)
        entry = None
        if id:
            entry = self.db.get("SELECT * FROM entries WHERE id= %s",int(id))
        self.render("compose.html",entry=entry)

    def post(self):
        id = self.get_argument("id",None)
        title = self.get_argument("title")
        text = self.get_argument("markdown")
        if id:
            pass
        else:
            slug = None
            if not slug:
                slug = "entry"
            self.db.execute("INSERT INTO entries (author_id,title,slug,markdown,html,published) VALUES (%s,%s,%s,%s,%s,UTC_TIMESTAMP())",1,title,slug,text,text)
        self.redirect("/entry/" + slug)


class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()