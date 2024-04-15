import machine
import time
import _thread
import pyRTOS

from onBoardLed import OnboardLed
from HCSR04 import SonicSensor
from buttonsPad import ButtonsPad
from extLed import LED

TRIG_PIN = 21
ECHO_PIN = 20
BUTTON_PINS = [13,14,15,16]
R_PIN = 19
G_PIN = 18

#semaphore = _thread.allocate_lock()
    
class System(object):
    def __init__(self):
        self.onBoardLed = OnboardLed()
        self.onBoardLed.turnOn()
        try:
            self.sonicSensor = SonicSensor(triggerPin=TRIG_PIN, echoPin=ECHO_PIN, echo_timeout_us=18000)
            self.buttonsPad = ButtonsPad(BUTTON_PINS)
            self.offBoardLed = LED(R_PIN, G_PIN)
            self.onBoardLed.turnOff()
        except OSError:
            OSError("Initialization Error")
            self.onBoardLed.turnOff()
            
        # create logical devices
        print('{}'.format('System Initiated'))
        
