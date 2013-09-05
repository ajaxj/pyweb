# -*- coding:utf-8 -*-
import threading
import time
from fetcher import Fetcher


# 多线程的操作类
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
    #初始化数据,比如 分类表
    # obj.initData()
    # 取出117 chuancai 保存mysql
    # datalist1 = obj.fromAccessToList(1)
    # for data in datalist1:
    #     print data[0]
    #     obj.insertDataToMySQL(data)

    # 取出118 yuecai
    # datalist2 = obj.fromAccessToList(2)
    # for data in datalist2:
    #     obj.insertDataToMySQL(data)

    # 取出119 xiangcai
    # datalist3 = obj.fromAccessToList(3)
    # for data in datalist3:
    #     obj.insertDataToMySQL(data)
    #
    # # 取出 120 jingcai
    # datalist4 = obj.fromAccessToList(4)
    # for data in datalist4:
    #     obj.insertDataToMySQL(data)


    print "save ok"

    #多线程的操作
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
