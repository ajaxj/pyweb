
# -*- coding:utf-8 -*-

# 取得当前版本
#import sqlalchemy
#print sqlalchemy.__version__
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://postgres:eeeeeeee@localhost:5432/fkapp')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
	__tablename__='users'
	
	id = Column(Integer,primary_key=True)
	nick = Column(String)
	email = Column(String)
	passwd = Column(String)

	def __init__(self,nick,email,passwd):
		self.nick = nick
		self.email = email
		self.passwd = passwd

	def __repr__(self):
		return "<User('%s')>" %(self.nick)


'''
if __name__ == '__main__':
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	session = Session()
	newuser = User('test1','test1@test.com','test1pass')
	session.add(newuser)
	session.flush()
	
	for row in session.query(User).all():
		print row.nick , row.email

	session.commit()
'''