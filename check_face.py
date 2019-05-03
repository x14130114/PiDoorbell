import RPi.GPIO as GPIO
from threading import Thread
from time import sleep
from facial_recogniton import FacialRecognition
from lock import Solenoid

fr = FacialRecognition()
lock = Solenoid()
id = 0
face = True

def counter():
    c = 0
    while c < 3:
        c = c + 1
        sleep(1)

def check():
    global face
    c = Thread(target=counter)
    c.daemon = True
    c.start()
    while c.is_alive():
        res = fr.recognize()
        if res is not None:
            print("%s, %s" % (id, res))
            if id != res[0]:
                face = False
                print (face)
            elif id == res[0] and res[1] > 85:
                face = False
                print (face)
                break

if __name__ == '__main__':
    while True:
        res = fr.recognize()
        print (res)
        if res is not None and res[1] < 80:
            id = res[0]
            face = True
            t = Thread(target=check)
            t.start()
            t.join()
            if face is True:
                Solenoid.unlock_door(21)
                #GPIO.cleanup()
                #face = Falseeee111111
                print(face)
                sleep(10)

#GPIO.cleanup()
