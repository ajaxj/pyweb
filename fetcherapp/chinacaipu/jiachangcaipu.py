# -*- coding:utf-8 -*-
'''
    http://www.chinacaipu.com/
    家常食谱
    水产类食谱 | 汤煲粥类食谱 | 肉类食谱 | 素食食谱 | 凉拌菜 | 禽类食谱 | 蛋类食谱
'''
import datetime
from pymongo import Connection
import win32com.client


class Jiachangcaipu:

    #读取火车头的ACCESS的表，返回list[id,title,content,分类]
    #dbname 一种菜谱access表,category string 分类
    def getCookFromAccess(self,dbname,category):
        list = []
        conn = None
        try:
            conn = win32com.client.Dispatch(r'ADODB.Connection')
            DSN = "PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%s;" %(dbname)
            conn.Open(DSN)
            rs = win32com.client.Dispatch(r'ADODB.Recordset')
            rs_name = 'Content'
            rs.Open(rs_name,conn,1,3)
            fields = {}
            rs.MoveFirst()
            while not rs.EOF:
                for x in range(rs.Fields.Count):
                    fields[x] = rs.Fields.Item(x).Value
                list.append([fields[0],fields[3],fields[4],category])
                rs.MoveNext()
        except Exception,e:
            print e
        finally:
            if conn != None:
                print 'conn.close'
                conn.Close()
        return list


    #把菜谱列表导入mongodb数据库
    def putCookListInMongodb(self,cook_list):
        try:
            conn  = Connection("localhost",27017)
            db = conn['cookbook']
            cooks = db['cooks']
            for data in cook_list:
                cook = {"title":data[1],"content":data[2],"data":datetime.datetime.utcnow()}
                cooks.insert(cook)
        except Exception,e:
            print e
        print "cooks ok"

    def mainrun(self):
        # 水产
        dbname = r"C:\data\shuichanshipu.mdb"
        category = "shuichan"
        cook_list = self.getCookFromAccess(dbname,category)
        self.putCookListInMongodb(cook_list)
        print "shuichan ok......"
        #汤煲粥
        dbname = r"C:\data\tangbaozhoushipu.mdb"
        category = "tangbaozhou"
        cook_list = self.getCookFromAccess(dbname,category)
        self.putCookListInMongodb(cook_list)
        print "tangbaozhuo ok......"
        #肉类
        dbname = r"C:\data\rouleishipu.mdb"
        category ="roulei"
        cook_list = self.getCookFromAccess(dbname,category)
        self.putCookListInMongodb(cook_list)
        print "roulei ok......"


if __name__ == "__main__":
    obj = Jiachangcaipu()
    obj.mainrun()