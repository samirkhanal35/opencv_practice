import cv2 as cv
import numpy as np

img = cv.imread('../basic_opencv/photos/cats.jpg')
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobely, sobelx)


cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("combined sobel", combined_sobel)

# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)


cv.waitKey(0)
