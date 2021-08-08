from time import sleep
from datetime import datetime
import random

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
    serial = spi(port=0, device=0, gpio=noop())
    #device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
    device = max7219(serial, width = WIDTH, height = HEIGHT, block_orientation=B_ORIENTATION, blocks_arranged_in_reverse_order=False)
    device.contrast(0)
    print("device created")
    
    matrix_face = Face(device)
    fimg = Image.open(r'/home/pi/Desktop/ProtoVIS-V1/matrix/components/face0.png')
    fimg = fimg.convert('1')
    matrix_face.showFace(fimg)
    print("started")

if __name__ == "__main__":
    main()