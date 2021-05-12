import cv2 as cv

img = cv.imread('photos/img1.jpeg')

# cv.imshow('image', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Blur image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# Edge Cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow("canny edges", cany)

# dialating the image
dilated = cv.dilate(cany, (7, 7), iterations=3)
cv.imshow("dialted image", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow("eroded image", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)
