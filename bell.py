
from picamera import PiCamera
from datetime import datetime
import time
from pushbullet import Pushbullet
from gpiozero import Button
from self import self

# connecting to push bullet api
pb = Pushbullet("o.xWndImaQeTc7WvQC6tK3yyTAJVdBKxrU")
# push = pb.push_note("Title","body")

# check the available devices
print(pb.devices)
# set your device
huawei = pb.get_device('HUAWEI HMA-L29')

class bellcam:
    now = datetime.now()
    button = Button(18)
    filename = ''

    def take_photo(self):
        global filename
        camera = PiCamera()
        # change this naming convention as it is not working
        filename = 'bell.jpg'
        camera.resolution = (800, 600)
        camera.capture('/home/pi/Desktop/cleaniot/' + (filename))
        camera.close()
        bellcam.push_notification(self)

    # when button is pressed, send_push notification to phone via pushbullet api
    def push_notification(self):
        print ('sending push notification with image...')
        with open("bell.jpg", "rb") as pic:
            img = pb.upload_file(pic, "Visitor at the door")
        huawei.push_file(**img)
        print ('sent........')

    def bell_pressed(self):
        while True:
            global camera
            print(bellcam.button.value)
            time.sleep(2)
            # button.when_released
            if bellcam.button.value is True:
                bellcam.take_photo(self)

    def set_btn(self):
        btn = bellcam.button.value
        #GPIO.cleanup()
        return btn

print ("END")
while True:
    bellcam.bell_pressed(self)

