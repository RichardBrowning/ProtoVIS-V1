
from picamera2 import Picamera2, Preview, Transform
from picamera2.output import CircularOutput
from picamera2.encoders import H264Encoder, Quality
import time
import datetime
from PIL import Image

class Camera:
    def __init__(self, resolution = (800, 480)):
        try:
            self.picam2 = Picamera2()
            # raise ValueError("An error occurred during initialization")
        except Exception as e:
            print(f"An error occurred: {e}")
            raise Exception("Picamera initialization failed")
        self.h264encoder = H264Encoder(10000000)

        ```
        "use_case"(only exist as aid): "preview", "still", "video"
        "transform": Transform()/Transform(hflip=1)/Transform(vflip=1)/Transform(hflip=1, vflip=1)
        "colour_space": Sycc()/Smpte170m()/Rec709()
        "buffer_count": 1,2,3,4...
        "display"(name of stream to be displayed in preview window): "main", "lores"
        "encode": "main", "lores"
        "sensor" (when used, determines sensor mode)
        "controls..."
        ```
        self.preview_config = picam2.create_preview_configuration(queue=True, lores={}, raw={"size": resolution}, transform=Transform(hflip=0, vflip=0))
        self.recording_config = picame2.create_recording_configuration(raw={"size": resolution})
        self.still_config = picam2.create_still_configuration(raw={"size": resolution})
        try:
            self.picam2.start_preview(Preview.DRM, width=resolution[0], height=resolution[1])
        except Exception as e:
            print(f"AN error occured: {e}")
            raise Exception("Preview starting failed")

    def __enter__(self):
        return self
    def __exit__(self):
        self.close()
  
    #def preview(self, durationSec, resolution):
    #    self.picam2.start()
    #    time.sleep(durationSec)
    #    self.picam2.stop()

    def start_preview(self):
        self.picam2.start_preview(Preview.DRM, width=resolution[0], height=resolution[1])
    def stop_preview(self):
        self.picam2.stop_preview()

    def capture_image(self, filename):
        # get pillow image
        image = self.picam2.switch_mode_and_capture_image(self.still_config)
        # save to file
        image.save("capture/images/" + filename)
        # self.picamera2.switch_mode_and_capture_array()

    def record_video(self, filename, duration):
        self.picam2.configure(self.recording_config)
        # output = FfmpegOutput("capture/videos/record" + datetime.datetime.now() + ".h264", audio=True)
        self.picamera2.start_recording(self.h264encoder, "capture/videos/record" + datetime.datetime.now() + ".h264", quality=Quality.HIGH)
        time.sleep(duration)
        self.picam2.stop_recording()
        self.picam2.configure(self.preview_config)
    
    # def record_circular_video(self, filename, duration):
        # TODO

    def close(self):
        self.picam2.close()
