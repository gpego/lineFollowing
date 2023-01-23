import cv2
import numpy as np


def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([0, 0, 0])
    upperWhite = np.array([179, 70, 255])
    maskWhite = cv2.inRange(img, lowerWhite, upperWhite)
    cv2.imshow("Vid", maskWhite)
    return maskWhite


def warpImg(img, points, w, h):
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp


def getHistogram(img, minPer = .1, display = False, region = 1):
    if region == 1:
        # Sum of the values of the pixels on the same column
        histValues = np.sum(img, axis = 0)
    else:
        # Sum of the values of the pixels on the same column for the first rows of the img
        # Var region used to know how many rows
        # Cropping the img
        histValues = np.sum(img[0 : (img.shape[0] // region),:], axis=0)

    maxValue = np.max(histValues)
    # Min val of color for each pixel, in order to delete random gray noises and have a clean path
    # minPer = percentage of maxValue under wich the pixel is discarded, default value = 10%
    minValue = minPer * maxValue

    # Return the sum of the columns that have pixels of the path
    indexArray = np.where(histValues >= minValue)
    # Point in the middle of the histogram
    basePoint = int(np.average(indexArray))

    # Displays histogram only if told in the function call
    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(histValues):
            # Hist line plotting
            cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - intensity // 255 // region), (255, 0, 255), 1)
            # Base point plotting
            cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
        return basePoint, imgHist
    
    return basePoint


#  Prominent Arduino map function :)
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)