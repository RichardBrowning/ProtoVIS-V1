import luma.emulator as em
import luma.emulator.device as dev
import time
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import ImageFont

def printInfo():
    print("Current Emulator Version: {}".format(em.__version__))

def main():
    printInfo()
    try:
        # emulator device initialization
        device = dev.pygame(width=32, height=24, rotate=0, mode='RGB')
        #(32, 24, 0, '1', 'scale2x', 2)
        with canvas(device) as draw:
            # draw rectangle on emulator device
            draw.rectangle(device.bounding_box, outline="white", fill="black")
        time.sleep(10)
    except AssertionError:
        print("Assertion Error")

if __name__ == '__main__':
    main()
