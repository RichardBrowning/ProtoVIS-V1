from module.Module import Module
# import module.ButtonHandler as ButtonHandler
from exceptions.ExceptionsSet import TerminateException, ResetCoreException
import time
import signal

BUTTONS = {"capture_image": 1, "mode_change": 24, "reset": 28, "power": 29}
MODES = ["Active", "Monitoring"]

class PVCore(object):
    def __init__(self, ):
        ## picamera2 #
        ## Speaker #
        ## 4-Buttons set #
        ## OLED display #
        ## TOF sensors #
        ## I2C controller
        ## LED strip 
        ## Microphone THIS WILL NOT BE DEVELOPED
        signal.signal(signal.SIGINT, self.signal_handler)
        self.FLAG_RUNNING = True
        self.m1 = Module(10, "interesting")
        self.m2 = Module(20, "boring")
        self.button_handlers = []
        #for name, pin in BUTTONS:
            #handler = ButtonHandler(pin, None)
            #self.button_handlers.append(handler)

    def loop(self):
        while self.FLAG_RUNNING:
            # get button status
            # run module's print
            print(self.m1.generateRandom())
            print(self.m1.getText())
            print(self.m2.generateRandom())
            print(self.m2.getText())
            time.sleep(0.05)
            
    def capture_image(self):
        print("Image captured\n")
    def mode_change(self):
        print("changed mode\n")
    def resets(self):
        print("Reset\n")
        raise ResetCoreException
    def halt(self):
        print("Program Halt\n")
        raise TerminateException

'''
if __name__ == "__main__":
    button_pin = 17  # Example GPIO pin number
    
    # Create an instance of ButtonHandler
    button_handler = ButtonHandler(button_pin, button_pressed_callback)
    
    try:
        # Keep the script running
        message = input("Press enter to quit\n\n")
    finally:
        GPIO.cleanup()  # Clean up at the end of your script
'''