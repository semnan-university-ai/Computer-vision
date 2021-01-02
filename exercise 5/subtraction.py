import cv2
import numpy as np
from PIL import Image

WAIT_KEY_DURATION = 10


def nothing(x):
    pass


def mean():
    cap = getCapture()
    images = []
    keepProcessing = True

    cv2.namedWindow('tracker')
    cv2.createTrackbar('val', 'tracker', 50, 255, nothing)
    backgroundOut = 0
    foregroundOut = 0
    while keepProcessing:
        ret, frame = cap.read()
        if ret == 0:
            keepProcessing = False
            continue

        showFrame(frame, 'Original Image', 50, 50)
        dim = (500, 500)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        # converting images into grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        images.append(frame_gray)
        # removing the images after every 50 image
        if len(images) == 50:
            images.pop(0)

        image = np.array(images)
        # gettting the tracker value
        val = cv2.getTrackbarPos('val', 'tracker')
        image = np.mean(image, axis=0)
        image = image.astype(np.uint8)
        showFrame(image, 'Mean Function Background', 600, 50)
        if backgroundOut == 0:
            im = Image.fromarray(image)
            height, width = im.size
            backgroundOut = writeOutput('mean_background_output.avi', width, height)
        backgroundOut.write(image)
        image = image.astype(np.uint8)
        # foreground will be background - curr frame
        foreground_image = cv2.absdiff(frame_gray, image)

        a = np.array([0], np.uint8)

        img = np.where(foreground_image > val, frame_gray, a)
        showFrame(img, 'Mean Function Foreground', 1200, 50)
        if foregroundOut == 0:
            im = Image.fromarray(img)
            height, width = im.size
            foregroundOut = writeOutput('mean_foreground_output.avi', height, width)
        foregroundOut.write(img)

        if cv2.waitKey(WAIT_KEY_DURATION) & 0xFF == 27:
            keepProcessing = False
    cap.release()
    cv2.destroyAllWindows()


def gmm():
    mog = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=16, detectShadows=True)
    cap = getCapture()
    keepProcessing = True
    out = 0

    while keepProcessing:
        if cap.isOpened:
            ret, frame = cap.read()
            if ret == 0:
                keepProcessing = False
                continue

            fgmask = mog.apply(frame)
            if out == 0:
                height, width, channels = frame.shape
                out = writeOutput(f'gmm_output_{width}x{height}.avi', width, height)
            out.write(fgmask)
            cv2.imshow('Gaussian Mixture Model Output', fgmask)
            key = cv2.waitKey(WAIT_KEY_DURATION) & 0xFF
            if key == ord('x'):
                keepProcessing = False
            elif key == ord(' '):
                print("\nResetting MoG background model ...\n")
                mog = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=16, detectShadows=True)

    cap.release()
    cv2.destroyAllWindows()


def getCapture():
    return cv2.VideoCapture('traffic.avi')


def showFrame(frame, name, x, y):
    cv2.namedWindow(name)
    cv2.moveWindow(name, x, y)
    cv2.imshow(name, frame)


def writeOutput(name, width=320, height=240):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    output = cv2.VideoWriter(name, fourcc, 20.0, (width, height), isColor=False)
    return output
