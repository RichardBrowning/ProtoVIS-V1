#!/usr/bin/env python
# coding=utf-8

import time
import cv2
from picamera2 import Picamera2, Preview
import numpy

picam = Picamera2(0)
config = picam.create_preview_configuration(queue=True, main={'size':(640, 480)})
picam.configure(config)

picam.start_preview(Preview.DRM, y=-60, width=800, height=600)
picam.start()

for time_left in range(10, 0, -1):
    colour = (0, 255, 0, 255)
    origin = (0, 90)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    thickness = 2
    overlay = numpy.zeros((640, 480, 4), dtype=numpy.uint8)
    cv2.putText(overlay, str(time_left), origin, font, scale, colour, thickness)
    picam.set_overlay(overlay)
    time.sleep(1)

picam.stop()
