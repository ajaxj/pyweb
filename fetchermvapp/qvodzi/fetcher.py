# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
import MySQLdb
import win32com.client

class Fetcher:
    #把dyzy的Access转人datalist
    def fromAccessToList(self):
        dbname = r"D:\projects\3tv3\98work\SpiderResult.mdb"
        conn = None
        list = []
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
                print fields[0]
                if fields[3] == None:
                    fields[3] = ""

                if fields[4] == None:
                    fields[4] = ""


                if fields[5] == None:
                    fields[5] = ""

                if fields[6] == None:
                    fields[6] = ''

                if fields[8] == None:
                    fields[8] = ''

                data = [fields[0],fields[3],fields[4],fields[5],fields[6],fields[8]]
                self.insertDataToMySQL(data)
                rs.MoveNext()
        except Exception,e:
            print e
        finally:
            if conn != None:
                print 'conn.close'
                conn.Close()


    #插入数据到MYSQL
    def insertDataToMySQL(self,data):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj1",charset="utf8")
        # sql = "SELECT * FROM mv_dyzy WHERE title = '%s' and url='%s'" %(data[1],data[3])
        # print sql + str(data[2])
        cur = conn.cursor()
        # cur.execute(sql)
        # if cur.fetchone() == None:
        sql = "INSERT INTO mv_qvodzi(title,oldcontent,lists,content,url)" \
                    " VALUES ('%s','%s','%s','%s','%s')" %(data[1].replace('\'','`'),data[2].replace('\'','`'),data[3].replace('\'','`'),data[4].replace('\'','`'),data[5])
        try:
            cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e
            exit(1)
        finally:
            cur.close()
            conn.close()


    def printContentById(self):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj1",charset="utf8")
        sql = "SELECT * FROM mv_qvodzi where id = 10388"
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        text = str(result[16])
        print u'text'
        cur.close()
        conn.close()


    #10387 10394,10402,11585,11600乱码
    def getContentById(self,id):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj1",charset="utf8")
        sql = "SELECT * FROM mv_qvodzi where id > 11600"
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            print result[0]
            if result[16] == '':
                pass
            else:
                soup =  BeautifulSoup(result[16])
                img = soup.find('img')
                if img == None:
                    _img = 'None'
                elif img.get('src') == None:
                    _img = 'None'
                else:
                    _img = img.get('src').replace('E:98/','')

                #TODO 10031挂了
                p_list = soup.findAll("p")
                _banben = p_list[1].text.replace(u'备注开始','').replace(u'备注结束','').split(":")[1]
                _status =  p_list[2].text.replace(u'连载开始','').replace(u'连载结束','').split(":")[1]
                _arts = p_list[3].text.replace(u'主演开始','').replace(u'主演结束','').split(":")[1]
                _dc =  p_list[4].text.replace(u'导演开始','').replace(u'导演结束','').split(":")[1]
                _location =  p_list[5].text.replace(u'地区开始','').replace(u'地区结束','').split(":")[1]
                _tp = p_list[6].text.replace(u'栏目开始','').replace(u'栏目结束','').split(":")[1]
                _year = p_list[7].text.replace(u'年代开始','').replace(u'年代结束','').split(":")[1]
                _lang =  p_list[8].text.replace(u'对白开始','').replace(u'对白结束','').split(":")[1]
                _pubdate = p_list[9].text.replace(u'时间开始','').replace(u'时间结束','').split(":")[1]

                if _banben == '': _banben = 'None'
                if _status == '': _status = 'None'
                if _arts == '':_arts = 'None'
                if _dc == '':_dc = 'None'
                if _location == '': _location = 'None'
                if _tp == '': _tp = 'None'
                if _year =='':_year = 'None'
                if _lang == '':_lang = 'None'
                if _pubdate=='':_pubdate='None'

                sql = "UPDATE mv_qvodzi SET img = '%s',location='%s',banben='%s',pubdate='%s',arts='%s',year='%s',lang = '%s',tp='%s',dc='%s',status='%s' WHERE id = %d" % (_img,_location,_banben,_pubdate,_arts,_year,_lang,_tp,_dc,_status,int(result[0]))
                cur.execute(sql)
                conn.commit()

        cur.close()
        conn.close()

if __name__ == '__main__':
    obj = Fetcher()
    # obj.fromAccessToList()
    obj.getContentById(1)
    # obj.printContentById()




