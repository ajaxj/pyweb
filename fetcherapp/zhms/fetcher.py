# -*- coding:utf-8 -*-
import MySQLdb
import win32com.client
from BeautifulSoup import BeautifulSoup


class Fetcher:

    # 解析acccess to list
    def fromAccessToList(self,cateid):
        if cateid == 1:
            dbname =r"E:\LocoySpider\Data\LocoySpider\117\SpiderResult.mdb"
            catestr = 'chuancai'
        elif cateid == 2:
            dbname =r"E:\LocoySpider\Data\LocoySpider\118\SpiderResult.mdb"
            catestr='yuecai'
        elif cateid == 3:
            dbname =r"E:\LocoySpider\Data\LocoySpider\119\SpiderResult.mdb"
            catestr='xiangcai'
        elif cateid == 4:
            dbname =r"E:\LocoySpider\Data\LocoySpider\120\SpiderResult.mdb"
            catestr='jingcai'
        elif cateid == 5:
            dbname =r"E:\LocoySpider\Data\LocoySpider\121\SpiderResult.mdb"
            catestr='lucai'
        elif cateid == 6:
            dbname =r"E:\LocoySpider\Data\LocoySpider\122\SpiderResult.mdb"
            catestr='mincai'
        elif cateid == 7:
            dbname =r"E:\LocoySpider\Data\LocoySpider\123\SpiderResult.mdb"
            catestr='huicai'
        elif cateid == 8:
            dbname =r"E:\LocoySpider\Data\LocoySpider\124\SpiderResult.mdb"
            catestr='zhecai'
        elif cateid == 9:
            dbname =r"E:\LocoySpider\Data\LocoySpider\125\SpiderResult.mdb"
            catestr='shucai'
        elif cateid == 10:
            dbname =r"E:\LocoySpider\Data\LocoySpider\126\SpiderResult.mdb"
            catestr='ecai'
        elif cateid == 11:
            dbname =r"E:\LocoySpider\Data\LocoySpider\127\SpiderResult.mdb"
            catestr='diancai'
        elif cateid == 12:
            dbname =r"E:\LocoySpider\Data\LocoySpider\128\SpiderResult.mdb"
            catestr='liaocai'
        elif cateid == 13:
            dbname =r"E:\LocoySpider\Data\LocoySpider\129\SpiderResult.mdb"
            catestr='sifangcai'
        else:
            dbname =r"E:\LocoySpider\Data\LocoySpider\117\SpiderResult.mdb"
            catestr = 'chuancai'

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
                list.append([fields[0],fields[3],fields[4],fields[8],catestr,cateid])
                rs.MoveNext()
        except Exception,e:
            print e
        finally:
            if conn != None:
                print 'conn.close'
                conn.Close()
        return list


    #插入数据到MYSQL
    def insertDataToMySQL(self,data):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="bangchubao",charset="utf8")
        sql = "SELECT * FROM zhms_caixi WHERE title = '%s' and url='%s'" %(data[1],data[3])
        # print sql + str(data[2])
        cur = conn.cursor()
        cur.execute(sql)
        if cur.fetchone() == None:
            sql = "INSERT INTO zhms_caixi(title,oldcontent,url,catestr,cateid)" \
                    " VALUES ('%s','%s','%s','%s','%d')" %(data[1].replace('\'','`'),data[2].replace('\'','`'),data[3],data[4],data[5])

            try:
                cur.execute(sql)
                conn.commit()
                print data[0]
            except Exception,e:
                print e
                exit(1)
            finally:
                cur.close()
                conn.close()


    #初始化表,比如分类表
    def initData(self):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="bangchubao",charset="utf8")
        cur = conn.cursor()
        try:
            data_list = []
            data_list.append([1,'川菜','chuancai'])
            data_list.append([2,'粤菜','yuecai'])
            data_list.append([3,'湘菜','xiangcai'])
            data_list.append([4,'京菜','jingcai'])
            data_list.append([5,'鲁菜','lucai'])
            data_list.append([6,'闽菜','mincai'])
            data_list.append([7,'徽菜','huicai'])
            data_list.append([8,'浙菜','zhecai'])
            data_list.append([9,'苏菜','shucai'])
            data_list.append([10,'鄂菜','ecai'])
            data_list.append([11,'滇菜','diancai'])
            data_list.append([12,'辽菜','liaocai'])
            data_list.append([13,'私房菜','sifangcai'])

            for data in data_list:
                sql = "INSERT INTO zhms_category(id,name,ename) VALUES ('%d','%s','%s')" %(data[0],data[1],data[2])
                cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e
            exit(1)
        finally:
            cur.close()
            conn.close()


    #通过分类取下面的CAIXI ID LIST
    def getCaixiIdListByCate(self,cate):
        list = []
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="bangchubao",charset="utf8")
        sql = "SELECT * FROM zhms_caixi WHERE catestr = '%s'" %(cate)
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        for r in results:
            list.append(r[0])
        cur.close()
        conn.close()
        return list



    #通过查找ID和更新图片字段
    def getContentByIdAndUpdateImg(self,id):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="bangchubao",charset="utf8")
        sql = "SELECT * FROM zhms_caixi WHERE id = %d" %(id)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()

        # print result[2]

        # 更新字段用的
        # print result[7], result[7].replace('E:NEWS/B','117')
        # if result[7] != 'None':
        #     _img = result[7].replace('E:NEWS/','')
        #     sql = "UPDATE zhms_caixi SET img = '%s' WHERE id = %d" % (_img,id)
        #     cur.execute(sql)
        #     conn.commit()


        # 查找Content里面有的IMG,
        soup = BeautifulSoup(result[2])
        img = soup.find('img')
        if img == None:
            _img = 'None'
        elif img.get('src') == None:
            _img = 'None'
        else:
             _img = img.get('src').replace('E:NEWS/','')

        sql = "UPDATE zhms_caixi SET img = '%s' WHERE id = %d" % (_img,id)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()



# test 测试修改图片
if __name__ == '__main__':
    obj = Fetcher()

    # obj.getContentByIdAndUpdateImg(2943)
    # exit(1)

    # id_list = obj.getCaixiIdListByCate('chuancai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update chuancai img ok"

    # id_list = obj.getCaixiIdListByCate('yuecai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update yuecai img ok"

    # id_list = obj.getCaixiIdListByCate('xiangcai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update xiangcai img ok"
    #
    #
    # id_list = obj.getCaixiIdListByCate('jingcai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update yuecai img ok"

    # id_list = obj.getCaixiIdListByCate('lucai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update lucai img ok"

    # id_list = obj.getCaixiIdListByCate('mincai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update mincai img ok"
    #
    # id_list = obj.getCaixiIdListByCate('huicai')
    # for id in id_list:
    #     obj.getContentByIdAndUpdateImg(id)
    #     print id
    # print "update huicai img ok"

    #

    id_list = obj.getCaixiIdListByCate('zhecai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update huicai img ok"


    id_list = obj.getCaixiIdListByCate('shucai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update shucai img ok"


    id_list = obj.getCaixiIdListByCate('ecai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update ecai img ok"


    id_list = obj.getCaixiIdListByCate('diancai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update diancai img ok"


    id_list = obj.getCaixiIdListByCate('liaocai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update liaocai img ok"

    id_list = obj.getCaixiIdListByCate('sifangcai')
    for id in id_list:
        obj.getContentByIdAndUpdateImg(id)
        print id
    print "update sifangcai img ok"




