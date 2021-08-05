import luma.emulator as em
import luma.emulator.device as device
import luma.emulator.render as render
import time
from PIL import Image
from luma.core.render import canvas
from luma.led_matrix.device import max7219
import pygame
from PIL import ImageFont

def printInfo():
    #TODO show info
    print("Current Emulator Version: {}".format(em.__version__))
def main():
    #Emulator Verison
    printInfo()

    '''Pygame Part
    #initiate pygame display
    screen = device.pygame(width=400, height=300, rotate=0, mode='1', transform='scale2x', scale=2)
    with canvas(screen) as draw:
        #draw a square
        draw.rectangle(screen.bounding_box, outline="white", fill="black")
    time.sleep(1)
    screen.clear()

    #set contrast
    time.sleep(1)
    screen.contrast(64)

    #set screen property(change size)
    screen.capabilities(width=360, height=270, rotate=0, mode='1')
    with canvas(screen) as draw:
        #draw a square
        draw.rectangle(screen.bounding_box, outline="white", fill="black")
    time.sleep(1)
    screen.clear()

    #re-set contrast
    screen.contrast(255)
    #clear pygame display
    screen.clear()
    #display image
    time.sleep(1)
    screen.capabilities(width=320, height=240, rotate=0, mode='1')
    img = Image.open('clockbirds.png')
    size = width, height = 320, 240
    img = img.resize(size)
    #print(img.show())
    screen.display(img)
    time.sleep(1)
    '''
    '''transformer'''
    #pygame initiation
    pygame.init()
    trans = render.transformer(pygame, width=32, height=24, scale=2)#transformer
    print(trans)

    #Surface initiation
    surf = pygame.Surface((32, 24))#surface
    matrix = trans.led_matrix(surf)
    print(matrix)
if __name__ == '__main__':
    main()