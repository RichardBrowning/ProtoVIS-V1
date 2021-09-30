from picamera import PiCamera
import time

camera = PiCamera()

camera.rotation = 180
camera.start_preview(alpha=255)
while True:
    com = input('Command(y/N):')
    if com == 'y' or com == 'Y':
        camera.stop_preview()
        break
    else:
        continue