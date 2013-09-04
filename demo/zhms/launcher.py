# -*- coding:utf-8 -*-
import threading
import time
from fetcher import Fetcher


class LauncherTime(threading.Thread):
    # 数据list 暂停时间
    def __init__(self,data_list,interval):
        threading.Thread.__init__(self)
        self.data_list = data_list
        self.interval = interval

    def run(self):
        for data in self.data_list:
            obj = Fetcher()
            obj.insertDataToMySQL(data)
            time.sleep(self.interval)




def main():
    obj = Fetcher()
    # obj.initData()
    datalist1 = obj.fromAccessToList(1)

    for data in datalist1:
        print data[0]
        obj.insertDataToMySQL(data)
    print "save ok"

    # datalist2 = obj.fromAccessToList(2)
    # datalist3 = obj.fromAccessToList(3)
    # thread1 = LauncherTime(datalist1,1)
    # thread2 = LauncherTime(datalist2,2)
    # thread3 = LauncherTime(datalist3,3)
    # thread1.start()
    # thread2.start()
    # thread3.start()





if __name__ == "__main__":
    main()
