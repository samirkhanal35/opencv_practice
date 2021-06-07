import cv2 as cv
import numpy as np


img = cv.imread("photos/img1.jpeg")

cv.imshow("image", img)

# Translation


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x ==> left
# -y ==> up
# x ==> Right
# y ==> Down


translated = translate(img, 100, 100)
cv.imshow("translated", translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    print(img.shape)
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow("rotated", rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# Flipping
# 0 => vertically
# 1 => horizontally
# -1 => both vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow("flipped", flip)


# cropping
cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)

#perspective Transformation
pts1 = np.float32([[56,165],[368,165],[28,587],[589,587]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img,M,(300,300))
cv.imshow("perspective", dst)

cv.waitKey(0)
