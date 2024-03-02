
from picamera2 import Picamera2, Preview
from libcamera import Transform
from picamera2.outputs import CircularOutput
from picamera2.encoders import H264Encoder, Quality
import time
import datetime
import cv2
import numpy

class Camera:
    def __init__(self, native_res=(640, 480)):
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
        
        self.preview_config = self.picam2.create_preview_configuration(queue=True, lores={'size': (int(native_res[0]/2), int(native_res[1]/2)), 'format': 'YUV420'}, main={'size': native_res, 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        self.recording_config = self.picam2.create_video_configuration(lores={'size': (int(native_res[0]/2), int(native_res[1]/2)), 'format': 'YUV420'}, main={'size': native_res, 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        self.still_config = self.picam2.create_still_configuration(lores={'size': (int(native_res[0]/2), int(native_res[1]/2)), 'format': 'YUV420'}, main={'size': native_res, 'format': 'XRGB8888'}, transform=Transform(hflip=0, vflip=0))
        
    def __enter__(self):
        return self
    def __exit__(self):
        self.close()
    
    def start_preview(self, resolution = (800, 480)):
        if self.picam2.camera_config is None:
            self.picam2.configure(self.preview_config)
        else:
            self.picam2.switch_mode(self.preview_config)
        self.picam2.start_preview(Preview.DRM, x=0, y=-int((resolution[0]*0.75-resolution[1])/2), width=resolution[0], height=int(resolution[0]*0.75))
        self.picam2.start()


    def stop_preview(self):
        self.picam2.stop_preview()

    def capture_image_previewing(self):
        # fileName = "capture/images/image" + datetime.datetime.now().ptrftime('%a%d%b%Y,%I:%M%p') + ".jpg"
        image = self.picam2.switch_mode_and_capture_file(self.still_config, "capture/images/image" + datetime.datetime.now().strftime('%a%d%b%Y,%I:%M%p') + ".jpg"
)

    def record_video(self, duration):
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
        # ------------------
        self.picam2.stop_recording()
        #self.picam2.stop_preview()
        # ------
        self.picam2.switch_mode(self.preview_config)
    
    # def record_circular_video(self, filename, duration):
        # Pending Decision: Too complicated implementation

    def add_overlay_text(self, edge_id, text, resolution=(800, 480)):
        if edge_id != 0 and edge_id != 1: 
            return
        if edge_id == 0:
            offset_y = 90
        else:
            offset_y = 60 + resolution[1]
        print(offset_y)
        color = (0, 255, 0, 255)
        origin = (0, offset_y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 1
        thickness = 2
        overlay = numpy.zeros((640, 480, 4), dtype=numpy.uint8)
        cv2.putText(overlay, str(text), origin, font, scale, color, thickness)
        self.picam2.set_overlay(overlay)

    
    def end_picam(self):
        self.picam2.start()
    
    def start_picam(self):
        self.picam2.stop()
