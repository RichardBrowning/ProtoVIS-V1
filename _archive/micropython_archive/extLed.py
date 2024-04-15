from machine import Pin

class LED(object):
    def __init__(self, rPin, gPin):
        self.redPin = Pin(rPin, Pin.OUT)
        self.greenPin = Pin(gPin, Pin.OUT)
        
    def breathGreen(self):
        print(' ')