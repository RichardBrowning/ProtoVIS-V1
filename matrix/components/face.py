from luma.led_matrix.device import max7219
from PIL import Image

from luma.core.legacy import text
from luma.core.legacy import show_message
from luma.core.legacy.font import ATARI_FONT, proportional, TINY_FONT, SEG7_FONT, UKR_FONT
from luma.led_matrix.device import max7219

import random
from time import sleep
from luma.core.render import canvas

class Face:
    def __init__(self, device:max7219):
        self.device = device
        #self.boot(self.device)
    def boot(self, device:max7219):
        show_message(device, msg = "Hello World!", fill = "white", font = SEG7_FONT, scroll_delay = 0.05)
        show_message(device, msg = "Here I Come!", fill = "white", y_offset=8, font=ATARI_FONT,  scroll_delay = 0.05)
        percent = list(range(0,101,1))
        breakpoint = list(random.sample(percent, 8))
        breakpoint.append(100)
        for p in percent:
	        #print(p)
            with canvas(device) as draw:
                text(draw, (1, 1), "Loading..." , fill="white", font = proportional(TINY_FONT))
                text(draw, (1, 8), (str(p)+"%") , fill="white", font = proportional(UKR_FONT))
            if p in breakpoint:
                if p == 100:
                    sleep(2)
                    device.clear()
                    break
                sleep(0.5)
                device.clear()
                continue
            sleep(0.02)
            device.clear()
    def showFace(self, face_image:Image):
        while True:
            self.device.display(face_image)
            i = input("Continue?(y/n)")
            if i == 'n' or i == 'N':
                break