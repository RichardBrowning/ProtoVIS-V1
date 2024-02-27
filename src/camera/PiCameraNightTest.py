from picamera import PiCamera
import time

camera = PiCamera()

#camera.rotation = 180
camera.start_preview(alpha=255)
#camera.annotate_background = Color('blue')
#camera.annotate_text = "Hello world"
camera.exposure_mode = 'off'
time.sleep(5)
camera.stop_preview()