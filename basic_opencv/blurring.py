# blurrring => smooting
import cv2 as cv

img = cv.imread("photos/cats.jpg")
cv.imshow("cats", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("average blur", average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("gaussian blur", gaussian)

# median Blur => salt and pepper noises
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# Bilateral Blurring => most effectinve
bilateral = cv.bilateralFilter(img, 8, 75, 75)
cv.imshow("bilateral", bilateral)


cv.waitKey(0)
