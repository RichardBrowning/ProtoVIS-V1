from config import BUTTON_PINS, BUTTON_FUNCS, RECORD_DUR, SLAVE_ADDR
from pyRTOS import Task

import time
from camera.Camera import Camera
from utils.I2CController import I2CController
from utils.ButtonHandler import ButtonHandler
from exceptions.ExceptionsSet import TerminateException, ResetCoreException

class PVCore(object):
    def __init__(self, ):
        ## picamera2 #
        ## OLED display #
        ## TOF sensors #
        ## I2C controller
        self.i2cController = I2CController();
        ## 4-Buttons set #
        self.MODE = 0
        self.button_handlers = [
            ButtonHandler(BUTTON_FUNCS[i], BUTTON_PINS[i], self.button_press_callback)
            for i in range(0, 4)
        ]
        self.i2c_controller = I2CController()
        # send mode to I2C controller
        self.i2c_controller.send_byte(self.MODE, SLAVE_ADDR)
        # start the camera
        self.picam = Camera()
        self.picam.start_preview()



    def loop(self):
        # if in active mode
        if self.MODE == 0:
            # TODO: read from the matrices, update the OLED display
            pass
        # if in passive mode
        elif self.MODE == 1:
            # Do nothing, for now, TODO: redesign
            pass

    def button_press_callback(self, button_id, duration):
        # if duration is less than 2 second, short press process
        if duration < 2:
            if button_id == BUTTON_PINS[0]:
                pass
            elif button_id == BUTTON_PINS[1]:
                # capture image
                self.capture_image()
            elif button_id == BUTTON_PINS[2]:
                pass
            elif button_id == BUTTON_PINS[3]:
                pass
        else:
            # if duration is more than 2 second, long press process
            if button_id == BUTTON_PINS[0]:
                # toggle self mode
                self.mode_change((self.MODE + 1) % 2)
            elif button_id == BUTTON_PINS[1]:
                self.capture_video(RECORD_DUR)
            elif button_id == BUTTON_PINS[2]:
                # reset the program
                self.resets()
            elif button_id == BUTTON_PINS[3]:
                # halt the program
                self.halt()
        
    def mode_change(self, mode):
        print("changed mode\n")
        # try sending mode to I2C controller
        try:
            self.i2c_controller.send_byte(mode)
            if mode == 0:
                print("Active Mode\n")
                # set preview ON
                self.picam.start_preview()
                # set TOFs & OLED Screen ON
                # set recognition OFF
            else:
                # set preview OFF
                self.picam.stop_preview()
                # TODO: set mode to recording mode ???? start recognition under mode

                # set TOFs & OLED Screen OFF
                # set recognition ON
            self.MODE = mode
        except:
            print("Failed to send mode to I2C controller\n")

    def capture_image(self):
        print("Image captured\n")
        self.picam.capture_image_preview()

    def capture_video(self):
        print("Video captured\n")
        self.picam.record_video(RECORD_DUR)






    # for CTRL+C handling
    def signal_handler(self, signal_received, frame):
        self.halt()
    
    # reset of program
    def resets(self):
        # send reset signal to I2C controller
        print("Reset\n")
        raise ResetCoreException
    # halt of program
    def halt(self):
        # send halt signal to I2C controller
        print("Program Halt\n")
        raise TerminateException