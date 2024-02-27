
import picamera
import time
class Camera:
    def __init__(self, resolution = (800, 480), framerate = 30):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
    
    def __enter__(self):
        return self
    def __exit__(self):
        self.close()
  
    def preview(self, durationSec):
        self.camera.start_preview()
        time.sleep(durationSec)
        self.camera.stop_preview()

    def capture_image(self, filename):
        self.camera.capture("capture/images/" + filename)

    def record_video(self, filename, duration):
        self.camera.start_recording("capture/video/" + filename)
        self.camera.wait_recording(duration)
        self.camera.stop_recording()

    def close(self):
        self.camera.close()
