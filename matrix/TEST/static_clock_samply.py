#!/usr/bin/env python
import sys
import time
import keyboard
from datetime import datetime
from threading import Thread
from itertools import cycle, chain

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT

'''NOTE THIS PROGRAM IS ONLY MEANT FOR MAX7219'''
WIDTH = 32
HEIGHT = 24
B_ORIENTATION = -90

GOON = True

def breath(device):
    breath_seq = chain(range(0,121,10), range(120,-1,-10))
    for i in cycle(breath_seq):
        #print(i)
        device.contrast(i)
        time.sleep(0.1)
        if GOON == False:
            break
'''
def animation(device):
'''

def showtime(device):
    toggle = False#秒
    while GOON == True:
        #秒的on and off
        toggle = not toggle
        #时间
        hours = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')
        #画
        with canvas(device) as draw:
            #draw.rectangle(device.bounding_box, fill = "black", outline="white")
            text(draw, (2, 1), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (14, 8), ":" if toggle else " ", fill="white", font=proportional(CP437_FONT))
            text(draw, (8, 16), minutes, fill="white", font=proportional(CP437_FONT))
        #print("Clock face initiated")
        time.sleep(0.5)

def stop():
    global GOON
    while True:
        com = input('Command(y/N):')
        if com == 'y' or com == 'Y':
            GOON = False
            break
        else:
            continue
    

def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial_r = spi(port=0, device=1, gpio=noop())#CE0
    serial_l = spi(port=0, device=0, gpio=noop())#CE1
    #device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
    device_r = max7219(serial_r, width = WIDTH, height = HEIGHT, block_orientation=B_ORIENTATION, blocks_arranged_in_reverse_order=False)
    device_r.contrast(0)
    print("device_r created")
    device_l = max7219(serial_l, width = WIDTH, height = HEIGHT, block_orientation=B_ORIENTATION, blocks_arranged_in_reverse_order=False)
    device_l.contrast(0)
    print("device_l created")
    
    threads = []
    threads.append(Thread(target=breath, args=(device_r,)))
    threads.append(Thread(target=breath, args=(device_l,)))
    threads.append(Thread(target=showtime, args=(device_r,)))
    threads.append(Thread(target=showtime, args=(device_l,)))
    threads.append(Thread(target=stop, args=()))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
