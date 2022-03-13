from constants import *
import argparse
import cv2
import dlib
import time
import imutils
from imutils.video import VideoStream
from imutils import face_utils


ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
args = vars(ap.parse_args())


print("-> Loading the predictor and detector...")


detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


print("-> Starting Video Stream")
vs = VideoStream(src=args["webcam"]).start()


time.sleep(1.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=850)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not(yawn):
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(
            30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        if(len(rects) == 0):
            cv2.putText(frame, "Face Not Found!", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        for (x, y, w, h) in rects:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
