import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    # images,videos, live videos
    width = int(frame.shape[1] * scale)  # 1=>width
    height = int(frame.shape[0] * scale)  # 0=>height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # live videos
    capture.set(3, width)
    capture.set(4, height)


# image resizing
img = cv.imread('photos/iris.jpg')
cv.imshow('iris', img)

resized_img = rescaleFrame(img)
cv.imshow('resized_iris', resized_img)

# video resizing
# capture = cv.VideoCapture('videos/video1.mp4')  # 0=>webcam

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video_resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
cv.waitKey(0)
