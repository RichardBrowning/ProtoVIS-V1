
from picamera2 import Picamera2, Preview
from libcamera import Transform
from picamera2.outputs import CircularOutput
from picamera2.encoders import H264Encoder, Quality
import time
import datetime
from PIL import Image

class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.h264encoder = H264Encoder(10000000)

        # "use_case"(only exist as aid): "preview", "still", "video"
        # "transform": Transform()/Transform(hflip=1)/Transform(vflip=1)/Transform(hflip=1, vflip=1)
        # "colour_space": Sycc()/Smpte170m()/Rec709()
        # "buffer_count": 1,2,3,4...
        # "display"(name of stream to be displayed in preview window): "main", "lores"
        # "encode": "main", "lores"
        # "sensor" (when used, determines sensor mode)
        # "controls..."
        
        self.preview_config = self.picam2.create_preview_configuration(queue=True, lores={'size': (320, 240), 'format': 'YUV420'}, main={'size': (640, 480), 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        self.recording_config = self.picam2.create_video_configuration(lores={'size': (320, 240), 'format': 'YUV420'}, main={'size': (640, 480), 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        self.still_config = self.picam2.create_still_configuration(lores={'size': (320, 240), 'format': 'YUV420'}, main={'size': (640, 480), 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        
    def __enter__(self):
        return self
    def __exit__(self):
        self.close()
    
    def _start_preview(self, resolution = (800, 480)):
        self.picam2.stop()
        self.picam2.start_preview(Preview.DRM, x=0, y=-(int(resolution[0]*0.75-resolution[1])), width=resolution[0], height=int(resolution[0]*0.75))
        self.picam2.configure(self.preview_config)
        self.picam2.start()


    def _stop_preview(self):
        self.picam2.stop_preview()
        self.picam2.stop()

    def capture_image_previewing(self):
        # fileName = "capture/images/image" + datetime.datetime.now().ptrftime('%a%d%b%Y,%I:%M%p') + ".jpg"
        image = self.picam2.switch_mode_and_capture_file(self.still_config, "capture/images/image" + datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p') + ".jpg"
)

    def record_video(self, filename, duration):
        self.picam2.stop()
        self.picam2.configure(self.recording_config)
        # output = FfmpegOutput("capture/videos/record" + datetime.datetime.now() + ".h264", audio=True)
        self.picam2.start_recording(self.h264encoder, "capture/videos/record" + datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p') + ".h264", quality=Quality.HIGH)
        time.sleep(duration)
        self.picam2.stop_recording()
    
    # def record_circular_video(self, filename, duration):
        # TODO

    def close(self):
        self.picam2.close()
