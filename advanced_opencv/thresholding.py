import cv2 as cv

img = cv.imread('../basic_opencv/photos/cats.jpg')
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded INVERSE', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive mean thresholding", adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive gaussian thresholding", adaptive_thresh_gaussian)

cv.waitKey(0)
