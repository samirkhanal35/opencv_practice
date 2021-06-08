import cv2 as cv
import numpy as np


img = cv.imread("photos/cats 2.jpg")
cv.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Imgae", blank)

# rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
# circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# bitwise_or = cv.bitwise_or(rectangle, circle)


mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

cv.waitKey(0)
