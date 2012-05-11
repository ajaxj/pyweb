from flaskext.script import Manager,Server
from sports import app
__author__ = 'window2003@gmail.com'

manager = Manager(app,with_default_commands=False)
manager.add_command("runserver", Server())


@manager.command
def hello():
    print "helloggg"


if __name__ == "__main__":
    manager.run()

