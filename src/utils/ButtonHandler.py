import RPi.GPIO as GPIO
import time

class ButtonHandler:
    def __init__(self, pin, callback, debounce=250):
        self.pin = pin
        self.callback = callback
        self.debounce = debounce
        self.button_pressed_time = 0
        self.button_released = True
        
        # set up button press time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # Note: Instead of detecting BOTH edges, we now separately add detection for RISING and FALLING
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.handle_press, bouncetime=self.debounce)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.handle_release, bouncetime=self.debounce)

    def handle_press(self, pin):
        # Mark the time when the button was pressed
        self.button_pressed_time = time.time()
        self.button_released = False

    def handle_release(self, pin):
        # Check if the button was previously pressed
        if not self.button_released:
            self.button_released = True
            current_time = time.time()
            # Trigger the callback function on release, PASS the pressed time
            self.callback(current_time - self.button_pressed_time)
