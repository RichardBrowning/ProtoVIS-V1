from picamera2 import Picamera2, Preview
from libcamera import Transform
from picamera2.outputs import CircularOutput
from picamera2.encoders import H264Encoder, Quality

import time
import datetime
import cv2
import numpy

class UsbCamera():
    def __init__(self):
        self.picam2 = Picamera2(1)
        self.h264encoder = H264Encoder(10000000)

        self.recording_config = self.recording_config = self.picam2.create_video_configuration(lores={'size': (int(native_res[0]/2), int(native_res[1]/2)), 'format': 'YUV420'}, main={'size': native_res, 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        self.still_config = self.picam2.create_still_configuration(lores={'size': (int(native_res[0]/2), int(native_res[1]/2)), 'format': 'YUV420'}, main={'size': native_res, 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))

        self.RECORDING_VIDEO = False

    def __enter__(self):
        return self
    def __exit__(self):
        self.close()

    def capture_image(self):
        picam2.start_and_capture_file("capture/images/usb_image" + datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p') + ".jpg")

    def capture_video(self):
        if self.RECORDING_VIDEO:
            return
        if self.picam2.is_open == False:
            return
        # ------
        if self.picam2.camera_config is None:
            self.picam2.configure(self.preview_config)
            self.picam2.start()
        else:
            self.picam2.switch_mode(self.recording_config)
        #self.picam2.start_preview()
        # ------------------
        self.picam2.start_recording(self.h264encoder, "capture/videos/record" + datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p') + ".h264", quality=Quality.HIGH)
        time.sleep(duration)
        self.RECORDING_VIDEO = True
        # ------------------
        self.picam2.stop_recording()
        self.RECORDING_VIDEO = False
        # ------
        self.picam2.switch_mode(self.preview_config)