#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import threading
import time

exitFlag = 0

class terThread (threading.Thread):
   def __init__(self, threadID):
      threading.Thread.__init__(self)
      self.threadID = threadID
   def run(self):
      print("Starting Driver Program")
      command(self.threadID)
      print("Exiting Driver Program")
# 为线程定义一个函数
def command(threadID,):
   global exitFlag
   #loop
   while True:
      # if endflag triggered
      if threadID == exitFlag:
         #end the task
         exitFlag = -1
         break
      #prompt user for input
      time.sleep(1)
      exitFlag = int(input("Input the thread ID of the task to exit: "))
      #set endFlag

def print_time(threadID, threadName, delay):
   print("starting " + threadName)
   global exitFlag
   while True:
      if exitFlag == threadID or exitFlag == -1:
         break
      time.sleep(delay)
      #print("%s === %s: %s" % (threadID, threadName, time.ctime(time.time())))
   print("exiting " + threadName)

def main():
   # 创建两个线程
   thread1 = threading.Thread(target = print_time, args=(1, "Mic", 0.5))
   thread2 = threading.Thread(target = print_time, args=(2, "Camera", 0.5))
   thread3 = threading.Thread(target = print_time, args=(3, "Display", 0.5))
   thread4 = threading.Thread(target = print_time, args=(4, "LED_Matrix", 0.5))
   thread5 = threading.Thread(target = print_time, args=(5, "Battery", 0.5))
   threadTer = terThread(6)
   threads = {thread1,  thread2, thread3, thread4, thread5, threadTer}

   for thread in threads:
      thread.start()

   print("Exiting Main Thread")

if __name__ == '__main__':
   main()