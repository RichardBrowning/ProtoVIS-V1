from machine import Pin

class ButtonsPad(object):
    def __init__(self, padPins):
        self.buttons = []
        for pin in padPins:
            self.buttons.append(Pin(pin, Pin.IN))
        
    def statusGenerator(self):
        for button in self.buttons:
            yield button.value()