import cv2 as cv

# img1 = cv.imread('photos/img1.jpeg')

# cv.imshow('image', img1)

capture = cv.VideoCapture('videos/video1.mp4')  # 0=>webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
