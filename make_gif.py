from picamera import PiCamera
from os import system

camera = PiCamera()

for i in range(10):
    camera.capture('/home/pi/Documents/timelapse/pictures_gif/image{0:04d}.jpg'.format(i))
    print('picture numer %d' % i)

print('creating animation')
system('convert -delay 10 -loop 0 /home/pi/Documents/timelapse/pictures_gif/image*.jpg /home/pi/Documents/timelapse/pictures_gif/animation.gif')
print('done')