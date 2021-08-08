import threading
import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT

from Clock import minute_change, animation, clock

command = "n"

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)
        
#def main():
while True: 
    command = input("Input command:")
    if command == "y" or command == "Y":
        threading._start_new_thread(clock())
        #TODO start new thread
        #clock()
    elif command == "n" or command == "N":
            

#if __name__ == "__main__":
    #main()