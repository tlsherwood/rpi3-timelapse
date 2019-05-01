"""
Fun with the Raspberry Pi3 camera
"""

from pathlib import Path


from time import sleep
import picamera

WAIT_TIME = 30

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    for filename in camera.capture_continuous('/home/pi/timelapse/img{timestamp:%Y%m%d_%H%M%S}.jpg'):
        sleep(WAIT_TIME)

