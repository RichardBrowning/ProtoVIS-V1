from machine import Timer
from sys import exit
from machine import reset
from system import System

import pyRTOS

system = System()
buttonsPressed = [1,1,1,1]

# def task1(self):
#     # Task1 setup here
#     yield
# 
#     while True:
#         # Task1 loop here
#         yield [pyRTOS.timeout(1)]           # Delay in seconds (Other task can run)
#         
# pyRTOS.add_task(pyRTOS.Task(task1))          # Add Task
# pyRTOS.start()                              # Start pyRTOS

def signal(self):
    #semaphore.acquire()
    global buttonsPressed
    yield
    while True:
        if buttonsPressed[0] == 0:
            #reset the reset button
            system.onBoardLed.toggle()
            buttonsPressed[0] = 1
        yield [pyRTOS.timeout(0.5)] #delay in seconds,
    #semaphore.release()
        
def buttonsListener(self):
    global buttonsPressed
    resetCount = 0
    yield
    while True:
        i = 0
        for buttonStatus in system.buttonsPad.statusGenerator():
            # if is the same as the last time, do not write in
            # if is 0, do not write 1 in
            if buttonsPressed[i] != buttonStatus:
                #if status is button pressed, but record is released
                if buttonStatus == 0 and buttonsPressed[i] == 1:
                    buttonsPressed[i] = buttonStatus
                    print (buttonsPressed)
            i += 1
            
        if buttonsPressed[3] == 0:
            resetCount += 1
            #reset the reset button
            buttonsPressed[3] = 1
            #reset()
            if resetCount > 5:
                exit()
        yield [pyRTOS.timeout(0.1)]
        
pyRTOS.add_task(pyRTOS.Task(buttonsListener))
pyRTOS.add_task(pyRTOS.Task(signal))
pyRTOS.start()

