from time import sleep
# import datetime
import picamera
# from picamera import PiCamera as camera

# event_duration is the time, in seconds, over which filming will occur.
# In other words, sunrise at 7AM thru sunset at 7PM would be a 12 hour event_duration or 12x3600=43200 seconds.
# video_length is the length of video desired (in seconds) assuming video frames per second (video_fps) settings.
# set event_duration OR video_length, not both. If using event_duration, video_length must be set to None.
# wait_time is the amount of time between photos (in seconds) and is used in conjunction with event_duration.
event_duration = 60
wait_time = 1
video_length = None
video_fps = 10

# The remaining code can be left as is unless something different is desired.
if video_length:
    number_of_pictures =  video_length * video_fps
else:
    number_of_pictures = event_duration / wait_time

with picamera.PiCamera() as camera:
    try:
        for picture, filename in enumerate(camera.capture_continuous('/home/pi/Documents/timelapse/pictures/img_{timestamp:%Y%m%d_%H%M%S}.jpg')):
            print('picture number %d of %d' % (picture, number_of_pictures))
            sleep(wait_time)
            if picture >= number_of_pictures:
                break
    finally:
        camera.close()
