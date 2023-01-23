import cv2
import numpy as np
import WarpingPointsUtils as utils

def getLaneCurve(img):

    imgCopy = img.copy()
    # Step 1
    imgThres = utils.thresholding(img)

    # Step 2
    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpImg(img, points, w, h)
    imageWarpPoints = utils.drawPoints(imgCopy, points)

    cv2.imshow("Thres", imgThres)
    cv2.imshow("Warp", imgWarp)
    cv2.imshow("Warp Points", imageWarpPoints)
    return None

# Check if this is the main module
if __name__ == '__main__':
    cap = cv2.VideoCapture(r"C:\Users\giovi\Desktop\RoboCup\Sync\myCode\lineFollowing\vids\VideoCapture01.mp4")
    initialTrackBarValues = [136, 85, 92, 233]
    utils.initializeTrackbars(initialTrackBarValues)

    frameCounter = 0
    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))   # Change resolution to 480 x 240 px
        getLaneCurve(img)

        cv2.imshow("Vid", img)  # Output the current frame
        cv2.waitKey(1)  # 1ms delay