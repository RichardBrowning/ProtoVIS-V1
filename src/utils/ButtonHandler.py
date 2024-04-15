import RPi.GPIO as GPIO
import time

class ButtonHandler:
    def __init__(self, id, pin, handler_callback, debounce=200):
        # 按钮 ID
        self.id = id
        # 按钮引脚
        self.pin = pin
        # 抖动时间阈值
        self.debounce = debounce
        # 按钮按下时的回调函数
        self.handler_callback = handler_callback
        self.button_pressed_time = 0
        self.button_released = True
        
        # set up button press time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # Note: Instead of detecting BOTH edges, we now separately add detection for RISING and FALLING
        # 按下按钮，触发下降沿函数handle_press
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.handle_press, bouncetime=self.debounce)
        # 松开按钮，触发上升沿函数handle_release
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.handle_release, bouncetime=self.debounce)

    def set_handler_callback(self, handler_callback):
        self.handler_callback = handler_callback

    def handle_press(self):
        # Mark the time when the button was pressed
        self.button_pressed_time = time.time()
        self.button_released = False

    def handle_release(self):
        # Check if the button was previously pressed
        if not self.button_released:
            self.button_released = True
            current_time = time.time()
            # Trigger the callback function on release, PASS the pressed time
            self.callback(self.id, current_time - self.button_pressed_time)
