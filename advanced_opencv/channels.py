import cv2 as cv
import numpy as np


img = cv.imread("../basic_opencv/photos/group.jpg")
cv.imshow("group", img)

print("shape[:2]", img.shape[:2])
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("blue img", blue)
cv.imshow("green img", green)
cv.imshow("red img", red)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)


cv.waitKey(0)
