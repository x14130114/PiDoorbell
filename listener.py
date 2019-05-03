# import alsaaudio
#from testkvs import Stream
#from train_face import trainFace
#from facial_recognition import FacialRecognition
#from facial_recogniton import FacialRecognition
import sys
from self import self
from firebase import Firebase
import RPi.GPIO as GPIO
from threading import Thread
from lock import Solenoid
from new_face import new_face
import time
import os

# creating objects for other methods in seperate classes
#fr = FacialRecognition()
# tface = trainFace()
nface = new_face()
door = Solenoid()
fb = Firebase()

class listener:
    print("in listener")

    # get method
    def get(self):
        # oldpos = ""
        while True:
            try:
                print("Starting the loop for checking values on Firebase")
                data = fb.get_data()
                # getting firebase values
                lock = data['doorbell']['lock']['state']
                face = data['doorbell']['face']['state']
                camera = data['doorbell']['camera']['state']
                audio = data['doorbell']['audio']['state']
                time.sleep(.5)
                print(lock)

                # checking if door has been unlockedd
                if lock == "open":
                    print ("The lock has been opened")
                    Solenoid.unlock_door(Solenoid.lock)
                    readings = {'doorbell/lock/state': "closed"}
                    fb.update_data(readings)

                # take pictures for new face recognition
                if face == "new":
                    print ("New face being added..")
                    nface.take_pictures()
                    print ("Face Added and Trained")
                    readings = {'doorbell/face/state': "added"}
                    fb.update_data(readings)
                """ elif face == "train":
                    print ("Face being trained")
                    tface.train_faces()
                    readings = {'doorbell/face/state': "trained"}
                    fb.update_data(readings)

                if camera == "start":
                    print ("camera start")
                    #p = subprocess.call(
                     #   'gst-launch-1.0 -v v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,width=640,height=480,framerate=30/1,format=I420 ! omxh264enc periodicty-idr=45 inline-header=FALSE ! h264parse ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! kvssink name=sink stream-name="test" access-key="AKIAIEKOVTSQMMS4JRTQ" secret-key="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" alsasrc device=hw:2,0 ! audioconvert ! avenc_aac ! queue ! sink.', shell=True)
                    #print(p)
                    #os.system("docker start bell")
                    #start_stream.start()
                    #time.sleep(20)
                    readings = {'doorbell/camera/state': "waiting"}
                    fb.update_data(readings)
                elif camera == "stop":
                    print ("camera stop")
                    os.system("docker stop bell")
                    readings = {'doorbell/camera/state': "waiting"}
                    fb.update_data(readings)"""

                if audio == "new":
                    fb.download_file()
                    print ("new audio")
                    #file = "audio.mp3"
                    # m = alsaaudio.Mixer("PCM")
                    # current_volume = m.getvolume()  # Get the current Volume
                    # m.setvolume(75)  # Set the volume to 70%.
                    # print (current_volume)
                    #os.system("mpg123 " + file)
                    os.system("omxplayer audio.mp3")
                    readings = {'doorbell/audio/state': "waiting"}
                    fb.update_data(readings)

            except KeyboardInterrupt:
                #p.stop()
                GPIO.cleanup()
                sys.exit(0)
                #threadGet.join()
                print ("Interrupted")

# running the main
if __name__ == '__main__':
    print("IN MAIN")
    # setup threads
    threadGet = Thread(target=listener.get(self))
        # start threads
    threadGet.start()
        # join threads
    threadGet.join()