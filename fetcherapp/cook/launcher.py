# -*- coding:utf-8 -*-



#主程
#   print obj.getNewsFormAccess.__doc__ 打印一个类的方法
import datetime
from pymongo import Connection
import win32com.client

# cook 应用
class Launcher:

    def getNewsFormAccess(self,dbname):
        '''
            读取火车头acccess返回一个新闻数据list[编号,新闻,内容]
        '''
        list = []
        conn = None
        try:
            conn = win32com.client.Dispatch(r'ADODB.Connection')
            DSN = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;" %(dbname)
            conn.Open(DSN)
            rs = win32com.client.Dispatch(r'ADODB.Recordset')
            rs_name = 'Content'
            rs.Open(rs_name,conn,1,3)
            fields = {}
            rs.MoveFirst()
            while not rs.EOF:
                for x in range(rs.Fields.Count):
                    fields[x] = rs.Fields.Item(x).Value
                list.append([fields[0],fields[3],fields[4]])
                rs.MoveNext()
        except Exception,e:
            print e
        finally:
            if conn != None:
                print 'conn.close'
                conn.Close()
        return list


    def getCooksFormAccess(self,dbname):
        '''
            读取火车头acccess返回一种菜谱的数据list[编号,title,内容]
        '''
        list = []
        conn = None
        try:
            conn = win32com.client.Dispatch(r'ADODB.Connection')
            DSN = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;" %(dbname)
            conn.Open(DSN)
            rs = win32com.client.Dispatch(r'ADODB.Recordset')
            rs_name = 'Content'
            rs.Open(rs_name,conn,1,3)
            fields = {}
            rs.MoveFirst()
            while not rs.EOF:
                for x in range(rs.Fields.Count):
                    fields[x] = rs.Fields.Item(x).Value
                list.append([fields[0],fields[3],fields[4]])
                rs.MoveNext()
        except Exception,e:
            print e
        finally:
            if conn != None:
                print 'conn.close'
                conn.Close()
        return list

    def putCookListInMongodb(self,cook_list):
        '''
            添加一个news_list进入mongodb数据库
        '''
        try:
            conn  = Connection("localhost",27017)
            db = conn['test']
            cooks = db['cooks']
            for data in cook_list:
                cook = {"title":data[1],"content":data[2],"data":datetime.datetime.utcnow()}
                cooks.insert(cook)
        except Exception,e:
            print e
        print "cooks ok"

    def putNewsListInMongodb(self,news_list):
        '''
            添加一个news_list进入mongodb数据库
        '''
        try:
            conn  = Connection("localhost",27017)
            db = conn['test']
            posts = db['posts']
            for data in news_list:
                post = {"title":data[1],"content":data[2],"data":datetime.datetime.utcnow()}
                posts.insert(post)
        except Exception,e:
            print e
        print "posts ok"

    #测试打印出一个find_one并取出一个title
    def test(self):
        try:
            conn  = Connection("localhost",27017)
            db = conn['test']
            posts = db['posts']
            print posts.find_one().get('title')
            cooks = db['cooks']
            print cooks.find_one().get('title')
        except Exception,e:
            print e



    def main(self):
        # 添加新闻数据进Mongodb
        # dbname = "D:\SpiderResult.mdb"
        # news_list = self.getNewsFormAccess(dbname)
        # self.putNewsListInMongodb(news_list)

        #添加cook进mongo
        # dbname = "D:\SpiderResult1.mdb"
        # cook_list = self.getCooksFormAccess(dbname)
        # self.putCookListInMongodb(cook_list)

        self.test()


if __name__ == "__main__":
    obj = Launcher()
    obj.main()
