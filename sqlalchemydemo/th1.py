# -*- coding:utf-8 -*-

# 最简单的线程调用

'''
import threading
import datetime

class ThreadClass(threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print "%s says Hello at time: %s" %(self.getName(),now)


for i in range(2):
	t = ThreadClass()
	t.start()
'''

#不用线程
'''
import urllib2
import time
hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com"]

start = time.time()
for host in hosts:
	url = urllib2.urlopen(host)
	print url.read(1024)

print " %s" %(time.time() - start)
'''
'''
import Queue
import threading
import urllib2
import time
hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com","http://ibm.com", "http://apple.com"]
queue = Queue.Queue()
class ThreadUrl(threading.Thread):
	"""Threaded Url Grab"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
		#grabs host from queue
			host = self.queue.get()
			#grabs urls of hosts and prints first 1024 bytes of page
			url = urllib2.urlopen(host)
			print url.read(1024)
			#signals to queue job is done
			self.queue.task_done()
          
start = time.time()
def main():
	for i in range(5):
		t = ThreadUrl(queue)
		t.setDaemon(True)
		t.start()
		 #populate queue with data   
		for host in hosts:
			queue.put(host)

	queue.join()
          
main()
print "Elapsed Time: %s" % (time.time() - start)

'''
'''
import threading  
import time  
class timer(threading.Thread):
	def __init__(self,num,interval):
		threading.Thread.__init__(self)
		self.thread_num = num
		self.interval = interval
		self.thread_stop = False

	def run(self):
		while not self.thread_stop:
			print "Thread Object(%d),Time:%s\n" %(self.thread_num,time.ctime())
			time.sleep(self.interval)

	def stop(self):
		self.thread_stop = True

def test():  
    thread1 = timer(1, 1)  
    thread2 = timer(2, 2)  
    thread1.start()  
    thread2.start()  
    time.sleep(10)  
    thread1.stop()  
    thread2.stop()  
    return  

test()

'''

import threading
import random
import time
from Queue import Queue

class Producer(threading.Thread):

    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name = threadname)
        self.sharedata = queue

    def run(self):
        for i in range(20):
            print self.getName(),'adding',i,'to queue'
            self.sharedata.put(i)
            time.sleep(random.randrange(10)/10.0)
        print self.getName(),'Finished'


# Consumer thread

class Consumer(threading.Thread):


    def __init__(self, threadname, queue):
        threading.Thread.__init__(self, name = threadname)
        self.sharedata = queue


    def run(self):

        for i in range(20):
            print self.getName(),'got a value:',self.sharedata.get()
            time.sleep(random.randrange(10)/10.0)
        print self.getName(),'Finished'


# Main thread

def main():

    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    print 'Starting threads ...'
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print 'All threads have terminated.'
if __name__ == '__main__':
    main()