from constants import *
from utils import *
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


detector = cv2.CascadeClassifier(
    "../models/haarcascade_frontalface_default.xml")
predictor = dlib.shape_predictor(
    '../models/shape_predictor_68_face_landmarks.dat')


print("-> Starting Video Stream")
vs = VideoStream(src=args["webcam"]).start()


time.sleep(1.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=850)
    # convert to grayscale colorspace
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not(yawn):
        # https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498
        # https://www.geeksforgeeks.org/cropping-faces-from-images-using-opencv-python/
        # arguments => image, scaleFactor, minNeighbors
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(
            30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # if face not found
        if(len(rects) == 0):
            cv2.putText(frame, "Face Not Found!", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        for (x, y, w, h) in rects:
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            distance = lip_distance(shape)

            lip = shape[48:60]
            cv2.drawContours(frame, [lip], -1, (0, 255, 0), 1)

            if (distance > YAWN_THRESH):
                cv2.putText(frame, "Yawn Alert", (650, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                alarm_status2 = False

            eye = final_ear(shape)
            ear = eye[0]
            leftEye = eye[1]
            rightEye = eye[2]

            # https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga014b28e56cb8854c0de4a211cb2be656
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            # https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < EYE_AR_THRESH:
                COUNTER += 1

                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    cv2.putText(frame, "DROWSINESS ALERT!", (100, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.imwrite("alert.png", frame)
                    time.sleep(1.0)
            else:
                COUNTER = 0
                alarm_status = False

            cv2.putText(frame, "EAR: {:.2f}".format(ear), (350, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "YAWN: {:.2f}".format(distance), (500, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
