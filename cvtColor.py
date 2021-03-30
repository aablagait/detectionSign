import cv2 as cv


def nothing(x):
    pass


cv.namedWindow('result')
color = cv.imread('spectr.jpg')

cv.createTrackbar('minb', 'result', 0, 255, nothing)
cv.createTrackbar('ming', 'result', 0, 255, nothing)
cv.createTrackbar('minr', 'result', 0, 255, nothing)

cv.createTrackbar('maxb', 'result', 0, 255, nothing)
cv.createTrackbar('maxg', 'result', 0, 255, nothing)
cv.createTrackbar('maxr', 'result', 0, 255, nothing)


while True:

    image = cv.imread('static/img_3.png')
    HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # HLS = cv.cvtColor(image, cv.COLOR_RGB2HLS)
    # YUV = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    cv.imshow('thrf', HSV)
    # minb = cv.getTrackbarPos('minb', 'result')
    # ming = cv.getTrackbarPos('ming', 'result')
    # minr = cv.getTrackbarPos('minr', 'result')
    #
    # maxb = cv.getTrackbarPos('maxb', 'result')
    # maxg = cv.getTrackbarPos('maxg', 'result')
    # maxr = cv.getTrackbarPos('maxr', 'result')

    mask = cv.inRange(HSV, (127, 106, 0), (255, 255, 255))
    # mask = mask.resize((50, 50))
    cv.imshow('mask', mask)

    frame_dilate = cv.dilate(mask, None, iterations=2)
    cv.imshow('frame_dilate', frame_dilate)
    contours, hierarchy = cv.findContours(frame_dilate.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    sort = []
    for i in contours:
        area = cv.contourArea(i)

        if 300 < area:  # можно регулировать дальность
            sort.append(i)

    cv.drawContours(image, sort, -1, (0, 255, 0), 2)
    cv.imshow('cont', image)





    if cv.waitKey(1) == 27:
        break



