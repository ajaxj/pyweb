# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
import MySQLdb
import win32com.client

class Fetcher:
    #把dyzy的Access转人datalist
    def fromAccessToList(self):
        dbname = r"D:\projects\3tv3\97work\SpiderResult.mdb"
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
                data = [fields[0],fields[3],fields[4],fields[8]]
                print data[0]
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
        sql = "INSERT INTO mv_dyzy(title,oldcontent,url)" \
                    " VALUES ('%s','%s','%s')" %(data[1].replace('\'','`'),data[2].replace('\'','`'),data[3])
        try:
            cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e
            exit(1)
        finally:
            cur.close()
            conn.close()



    # 17651 17661 17671 17884 17893 18303 18313 19459
    def getContentById(self,id):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj1",charset="utf8")
        sql = "SELECT * FROM mv_dyzy where id > 19459"
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            soup = BeautifulSoup(result[16])
            img = soup.find('img')
            if img == None:
                _img = 'None'
            elif img.get('src') == None:
                _img = 'None'
            else:
                _img = img.get('src').replace('E:97/','')

            content = soup.find('div',{'id':'movieContent'})

            if content  == None:
                _content = 'None'
            elif content.text ==  None:
                _content = 'None'
            else:
                _content = content.text



            p_list = soup.findAll("p")
            _tp =  p_list[1].text.split(":")[1]
            _location =  p_list[2].text.split(":")[1]
            _status =  p_list[3].text.split(":")[1]
            _banben =  p_list[4].text.split(":")[1]
            _arts =  p_list[5].text.split(":")[1]
            _dc =  p_list[6].text.split(":")[1]
            _year  = p_list[7].text.split(":")[1]
            _pubdate = p_list[8].text.split(u"间:")[1]

            if _tp == '': _tp = 'None'
            if _location == '': _location = 'None'
            if _status == '': _status = 'None'
            if _banben == '': _banben = 'None'
            if _arts == '':_arts = 'None'
            if _dc == '':_dc = 'None'
            if _year =='':_year = 'None'
            if _pubdate=='':_pubdate='None'

            sql = "UPDATE mv_dyzy SET img = '%s',location='%s',banben='%s',pubdate='%s',arts='%s',year='%s',content='%s',tp='%s',dc='%s',status='%s' WHERE id = %d" % (_img,_location,_banben,_pubdate,_arts,_year,_content,_tp,_dc,_status,int(result[0]))
            cur.execute(sql)
            conn.commit()
            print result[0]

        cur.close()
        conn.close()




if __name__ == '__main__':
    obj = Fetcher()
    # obj.fromAccessToList()
    obj.getContentById(1)






