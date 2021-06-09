import cv2 as cv

img = cv.imread('../basic_opencv/photos/cats.jpg')
cv.imshow("cats", img)


cv.waitKey(0)
