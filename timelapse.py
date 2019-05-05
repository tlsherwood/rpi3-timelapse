from time import sleep
# import datetime
import picamera
# from picamera import PiCamera as camera

"""VIDEO_LENGTH is the length of video desired (in seconds) assuming frame per second (FPS) settings"""
VIDEO_LENGTH = 60
FPS = 15

"""the remaining code can be left as is unless something different is desired"""
"""WAIT_TIME is the amount of time between photos (in seconds)"""
WAIT_TIME = 2.5
number_of_pictures = FPS * VIDEO_LENGTH

with picamera.PiCamera() as camera:
    try:
        for picture, filename in enumerate(camera.capture_continuous('/home/pi/timelapse/img_{timestamp:%Y%m%d_%H%M%S}.jpg')):
            sleep(WAIT_TIME)
            if picture == number_of_pictures:
                break
    finally:
        camera.close()
