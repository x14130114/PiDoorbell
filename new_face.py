from time import sleep
from facial_recogniton import FacialRecognition
import os
import cv2
import random

fr = FacialRecognition()

class new_face:

    # the user registration process
    def take_pictures(self):
        # time countdown before take the picture (5s)
        ct = 5
        #Console.clear()
        while ct > 0:
            print('Please look at the camera now. We will take a few pictures in: %s' % ct)
            sleep(1)
            ct = ct - 1
            os.system('clear')

        # check if folder already exists
        if os.path.exists('user') is False:
            os.mkdir('user')

        # get random id and if exists re-randomize again
        user_id = random.SystemRandom().randint(10000, 99999)
        while True:
            if os.path.exists('user/%s' % user_id) is False:
                os.mkdir('user/%s' % user_id)
                break
            else:
                user_id = random.SystemRandom().randint(10000, 99999)

        counter = 0  # will count pictures which were taken

        # taking user's pictures
        while True:
            ret, frame = fr.video.read()  # ret - bool, frame - current camera frame
            gray = fr.convert_to_grey(frame)  # convert picture to greyscale
            faces = fr.cascade.detectMultiScale(gray, 1.5, 5)  # detect faces

            # iterate through detected
            for (x, y, w, h) in faces:
                cv2.imwrite("user/%s/%s.jpg" % (user_id, counter), gray[y: y + h, x: x + w])
                counter = counter + 1

            if counter == 40:  # at the 10th picture stop
                fr.train_faces()  # run train algorithm

                # print successful message
                #Console.clear()
                print('Your profile was created! Thanks!')
                sleep(3)
                break
