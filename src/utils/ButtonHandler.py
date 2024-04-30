from gpiozero import Button
import time

class ButtonHandler:
    def __init__(self, id, pin, handler_callback):
        # 按钮 ID
        self.id = id
        self.button_pressed_time = None
        self.button_released_time = None
        # 按钮按下时的回调函数
        self.handler_callback = handler_callback
        # set up button press time
        self.button = Button(pin)
        self.button.when_pressed = self.handle_press
        self.button.when_released = self.handle_release

    def set_handler_callback(self, handler_callback):
        self.handler_callback = handler_callback

    def handle_press(self):
        # Mark the time when the button was pressed
        self.button_pressed_time = time.time()

    def handle_release(self):
        self.button_released_time = time.time()
        # Calculate the duration of the button press
        duration = self.button_released_time - self.button_pressed_time
        # Test output
        print(f"Button {self.id} pressed for {duration} seconds")
        # Call the handler callback function
        self.handler_callback(self.id, duration)

