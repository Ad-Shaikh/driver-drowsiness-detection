import cv2

# Importing Harcascade Models
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade_left = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
eye_cascade_right = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')


# function takes an image input and detects a face and will return co-ordinates of rectangle around face
def detect_one_face(im):
    # convert to grayscale colorspace
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498
    # https://www.geeksforgeeks.org/cropping-faces-from-images-using-opencv-python/
    # arguments => image, scaleFactor, minNeighbors
    faces = face_cascade.detectMultiScale(gray, 1.2, 3)
    # scaleFactor => how much the image size is reduced at each image scale => https://answers.opencv.org/question/10654/how-does-the-parameter-scalefactor-in-detectmultiscale-affect-face-detection/
    # minNeighbors Parameter specifying how many neighbors each candidate rectangle should have to retain it => https://stackoverflow.com/questions/22249579/opencv-detectmultiscale-minneighbors-parameter

    # if face not found
    if len(faces) == 0:
        return (0, 0, 0, 0)

    # if face is found => assuming the driver is always only one face
    return faces[0]
