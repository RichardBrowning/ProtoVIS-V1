from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
#from luma.core.virtual import viewport
from luma.core.legacy import text
from luma.core.legacy.font import proportional, TINY_FONT
'''
ATARI_FONT
Designed for a terminal emulator written for an Atari 800.
http://gnu.ethz.ch/linuks.mine.nu/atari/

CP437_FONT
See https://en.wikipedia.org/wiki/Code_page_437 for further details.
unascribed

LCD_FONT
Only contains characters 0x20-0x7F inclusive and Cyrillic chars 0x80-0xBF (except ‘Ёё’); all others will appear as blanks.
http://www.avrfreaks.net/forum/code-57-512-and-712-fonts?name=PNphpBB2&file=viewtopic&t=69880

SEG7_FONT
Only contains characters 0x41-0x5A & 0x30-0x39 inclusive; all others will appear as blanks.
https://www.dafont.com/digital-7.font

SINCLAIR_FONT
Based on the character set from the Sinclair ZX Spectrum. Only contains characters 0x20-0x7E inclusive; all others will appear as blanks.
http://www.henningkarlsen.com/electronics/r_fonts.php

SPECCY_FONT
Another font based on the character set from the ZXSpectrum.
https://www.kreativekorp.com/software/fonts/index.shtml

TINY_FONT
Only contains characters 0x20-0x7E inclusive; all others will appear as blanks.
https://www.dafont.com/tiny.font

UKR_FONT
Cyrillic Ukrainian font
'''
from luma.led_matrix.device import max7219
import time

def frame(width, height, block_orientation, rotate, inreverse):
    #size of LED matrix is 64*24
    # create matrix device
    serial_r = spi(port=0, device=0, gpio=noop())
    serial_l = spi(port=0, device=1, gpio=noop())
    #对于非一维排列的matrix, casecade可能是没有用的
    device_l = max7219(serial_l, width = width, height = height, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    device_r = max7219(serial_r, width = width, height = height, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")
    device_r.contrast(0)
    device_l.contrast(0)
    with canvas(device_r) as draw:
        draw.rectangle(device_r.bounding_box, fill = "white", outline="black")
        text(draw, (1, 2), "Hello", fill="white", font = proportional(TINY_FONT))
        text(draw, (1, 10), "World", fill="white", font = proportional(TINY_FONT))
    with canvas(device_l) as draw:
        draw.rectangle(device_l.bounding_box, fill = "white", outline="black")
        text(draw, (1, 2), "Hello", fill="white", font = proportional(TINY_FONT))
        text(draw, (1, 10), "World", fill="white", font = proportional(TINY_FONT))
    time.sleep(10)

if __name__ == "__main__":
    width = 32
    height = 24
    block_orientation = -90
    rotate = 0
    inreverse = False

    frame(width, height, block_orientation, rotate, inreverse)