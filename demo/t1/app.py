
from pymongo import Connection
import win32com.client


def test_mongo():
    connection = Connection("localhost",27017)
    print connection.database_names()   #['u'local',u'test']
    db = connection.test
    print db.collection_names()

def test_access():
    list = []
    conn = None
    try:
        conn = win32com.client.Dispatch(r'ADODB.Connection')
        DSN = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\SpiderResult.mdb;"
        conn.Open(DSN)
        rs = win32com.client.Dispatch(r'ADODB.Recordset')
        rs_name = 'Content'
        rs.Open(rs_name,conn,1,3);
        flds = {}
        rs.MoveFirst()
        count = 0
        while not rs.EOF:
            for x in range(rs.Fields.Count):
                flds[x] = rs.Fields.Item(x).Value
            #print "|   %s|    %s|  %s|" % (flds[0],flds[3],flds[4])
            #count = count + 1
            rs.MoveNext()
        #print "Record Count:%d" % (count)
    except Exception,e:
        print e
    finally:
        if conn != None:
            print "conn close"
            conn.Close()



if __name__ == "__main__":
    # test_mongo()
    test_access()


