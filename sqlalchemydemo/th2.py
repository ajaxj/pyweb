# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
import urllib2
from th3 import *
import threading
import time
import HTMLParser
import os


# 读取地图的页面取得各地区的连接
def getUrlList():
	area_list =[]
	try:
		url = "http://www.lvchengba.com/jingdianAll/1001"
		d = pq(url)
		for area in d('area'):
			area_list.append(pq(area).attr('href'))
		print 'success'
	except:
		print 'err getUrList'
		
	return area_list


#保存各地连接URL网址和内容
def saveUrlAndContentToDb(url,content):
	lv = Lvchengba()
	lv.url = url
	lv.content = content
	session = Session()
	session.add(lv)
	session.flush()
	session.commit()


#解析连接并插入数据库线程
class InsertDatabase(threading.Thread):
	def __init__(self,threadname,area_list):
		threading.Thread.__init__(self,name=threadname)
		self.area_list = area_list

	def run(self):
		for href in self.area_list:
			url = 'http://www.lvchengba.com'+ href;
			req = urllib2.Request(url)
			req.add_header('User-Agent','ajaxj')
			res = urllib2.urlopen(req)
			htmlstr = res.read()
			saveUrlAndContentToDb(url,htmlstr.decode('gbk').encode('utf-8'))
			print self.getName(), 'insert database',href
			time.sleep(5)
		print self.getName(),'Finished'


#解析连接并保存页面线程
class SaveUrl(threading.Thread):
	def __init__(self,threadname,area_list):
		threading.Thread.__init__(self,name=threadname)
		self.area_list = area_list

	def run(self):
		for href in area_list:
			filename = os.getcwd() + "\\temp\\" +  href.replace('/','_') + '.html'
			url = 'http://www.lvchengba.com'+ href;
			req = urllib2.Request(url)
			req.add_header('User-Agent','ajaxj')
			res = urllib2.urlopen(req)
			htmlstr = res.read()
			df = open(filename,'w')
			df.write(htmlstr.decode('gbk').encode('utf-8'))
			df.flush()
			df.close()
			print self.getName(),'save url',url
			time.sleep(3)
		print self.getName(),'Finished'



if __name__ == '__main__':
	#运行线程
	area_list = getUrlList()
	obj1 = InsertDatabase('obj1',area_list)
	obj2 = SaveUrl('obj2',area_list)
	obj1.start()
	obj2.start()
	obj1.join()
	obj2.join()



