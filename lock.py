import RPi.GPIO as GPIO
import time

lock = 21
# change the sleep timer for how long the door stays open and use a slider on the app to modify it
class Solenoid:
    lock = 21

    def unlock_door(lock):
        print ("in lock")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(lock, GPIO.OUT)
        GPIO.output(lock, GPIO.LOW)  # Turn motor on
        time.sleep(5)
        GPIO.cleanup(21)
        print ("finish")

    #if __name__ == '__main__':
    #    try:
    #        unlock_door(lock)
    #        time.sleep(1)
    #        GPIO.cleanup()
    #    except KeyboardInterrupt:
    #        GPIO.cleanup()

#Solenoid.unlock_door(lock)