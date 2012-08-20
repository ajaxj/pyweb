# -*- coding:utf-8 -*-

# 取得当前版本

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:eeeeeeee@localhost:5432/fkapp')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Lvchengba(Base):
	__tablename__ = 'lvchengba'
	
	id = Column(Integer,primary_key=True)
	lvid = Column(Integer)
	lvname = Column(String)
	url = Column(String)
	content = Column(Text)

	#def __init__(self,url):
	#	self.url = url

	def __repr__(self):
		return self.url


#景点模型
class Jingdian(Base):
	__tablename__ = 'jingdian'
	id = Column(Integer,primary_key=True)
	lvid = Column(Integer)
	title = Column(String)
	url = Column(String)
	content = Column(Text)

	def __repr__(self):
		return self.title

class Dpcity(Base):
    __tablename__ = 'dp_citys'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    pinyin   = Column(String)
    en = Column(String)
    cid = Column(Integer)
    homepage = Column(String)




#初始化数据库
def initDB():
	print 'initDB'
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	#session = Session()
	#session.query(Lvchengba).all()
	#lv  = Lvchengba()
	#lv.url = 'url1'
	#lv.content = 'content1'
	#session.add(lv)
	#session.flush()
	#session.commit()


if __name__ == '__main__':
	# 直接生成表
	print 'initdb run'		
	initDB()