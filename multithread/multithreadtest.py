#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import threading
import time
from tkinter import Y

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, taskName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.taskName = taskName
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, self.taskName, 3)
      print("Exiting " + self.name)

class terThread (threading.Thread):
   def __init__(self, threadID, name, taskName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.taskName = taskName
   def run(self):
      print("Starting " + self.name)
      #TODO
      print("Exiting " + self.name)

# 为线程定义一个函数
def print_time( threadName, taskName, delay):
   while True:
      if exitFlag:
         (threading.Thread).exit()
      time.sleep(delay)
      print("%s === %s: %s" % (taskName, threadName, time.ctime(time.time()) ))

# 创建两个线程
thread1 = myThread(1, "Alpha", "Mic")
thread2 = myThread(2, "Beta", "Camera")
thread3 = myThread(3, "Gamma", "Display")
thread4 = myThread(4, "Theta", "LED_Matrix")
thread5 = myThread(5, "Omega", "Battery")
thread6 = terThread()
threads = {thread1,  thread2, thread3, thread4, thread5}

for thread in threads:
   thread.start()

print("Exiting Main Thread")