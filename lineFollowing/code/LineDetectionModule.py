import cv2
import numpy as np
import utils


"""
curveList = []
avgVal = 10 # Max number of elements in curveList
"""

# Line filtering
def getLaneCurve(img):

    # Step 1
    imgThres = utils.thresholding(img)

    # Step 2
    h, w, c = img.shape
    # Values from WarpingPointsCalculation.py, use to calibrate
    xy = np.array([136, 85, 92, 233])
    wT = img.shape[1]    # Screen width
    # Warp points determination from xy array's values
    points = np.float32([(xy[0], xy[1]), (wT-xy[0], xy[1]),
                      (xy[2] , xy[3] ), (wT-xy[2], xy[3])])
    imgWarp = utils.warpImg(imgThres, points, w, h) # Warp the img

    # Step 3
    middlePoint, imgHist = utils.getHistogram(imgWarp, display = True, minPer = .5, region = 2)
    curveAveragePoint, imgHist = utils.getHistogram(imgWarp, display = True, minPer = .5)
    curveRaw = curveAveragePoint - middlePoint

    # Step 4: Averaging
    """
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))
    """

    curve = curveRaw

    # Normalization: taking the value in the range frm -1 to +1
    curve = curve / 100
    if curve > 1: curve == 1
    elif curve < -1: curve == -1

    cv2.imshow("Thres", imgThres)
    cv2.imshow("Warp", imgWarp)
    cv2.imshow("Hist", imgHist)

    return curve


# Check if this is the main module
if __name__ == '__main__':
    cap = cv2.VideoCapture(r"C:\Users\giovi\Desktop\RoboCup\Sync\myCode\lineFollowing\vids\VideoCapture01.mp4")
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (480, 240))   # Change resolution to 480 x 240 px
        getLaneCurve(img)

        cv2.imshow("Vid", img)  # Output the current frame
        cv2.waitKey(1)  # 1ms delay