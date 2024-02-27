from time import sleep
from datetime import datetime
import random

from threading import Thread
from PIL import Image 
from components.face import Face

#interface
from luma.core.interface.serial import spi, noop
#render
from luma.led_matrix.device import max7219

'''NOTE THIS PROGRAM IS ONLY MEANT FOR MAX7219'''
WIDTH = 32
HEIGHT = 24
B_ORIENTATION = -90

def main():
    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial_l = spi(port=0, device=0, gpio=noop())
    serial_r = spi(port=0, device=1, gpio=noop())
    #device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
    device_l = max7219(serial_l, width = WIDTH, height = HEIGHT, block_orientation=B_ORIENTATION, blocks_arranged_in_reverse_order=False)
    device_r = max7219(serial_r, width = WIDTH, height = HEIGHT, block_orientation=B_ORIENTATION, blocks_arranged_in_reverse_order=False)
    device_l.contrast(0)
    device_r.contrast(0)
    print("device created")
    #simultaneous show start message
    threads = []
    matrix_face_l = Face(device_l)
    matrix_face_r = Face(device_r)
    fimg = Image.open(r'/home/pi/Desktop/ProtoVIS-V1/matrix/components/face0.png')
    #fimg = fimg.convert('1')
    threads.append(Thread(target=matrix_face_l.boot, args=()))
    threads.append(Thread(target=matrix_face_r.boot, args=()))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    #simultaneous show face
    threads.clear()
    threads.append(Thread(target=matrix_face_l.showFace, args=(fimg))) 
    threads.append(Thread(target=matrix_face_r.showFace, args=(fimg))) 
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("started")

if __name__ == "__main__":
    main()