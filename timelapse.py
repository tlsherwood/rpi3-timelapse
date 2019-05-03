from time import sleep
import datetime
import picamera
from picamera import PiCamera as camera

"""video_length_seconds is the length of video desired (in seconds) assuming fps settings"""
video_length_seconds = 30
fps = 30

"""the remaining code can be left as is unless something different is desired"""
"""WAIT_TIME is the amount of time between photos"""
WAIT_TIME = 10
number_of_pictures = fps * video_length_seconds

with picamera.PiCamera() as camera:
    try:
        for picture, filename in enumerate(camera.capture_continuous('/home/pi/timelapse/img_{timestamp:%Y%m%d_%H%M%S}.jpg')):
            sleep(WAIT_TIME)
            if picture == number_of_pictures:
                break
    finally:
        camera.close()
