import cv2 as cv


def detectionRED(frame):
    """ В качестве аргумента функция принимает кадр, переводит в цветовой формат hsv,
    накладывает маску только красного цвета, сглаживает области и находит контуры.
    Цикл оставляет контуры, подходящие по размеру, и отрисовывает их.
    Функция возвращает кадр, спше нарисованными контурами"""
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_mask = cv.inRange(frame_hsv, (127, 106, 0), (255, 255, 255))
    frame_dilate = cv.dilate(frame_mask, None, iterations=2)
    contours, hierarchy = cv.findContours(frame_dilate.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    sort = []
    for i in contours:
        area = cv.contourArea(i)

        if 400 < area < 1500:  # можно регулировать дальность
            sort.append(i)

    cv.drawContours(frame, sort, -1, (0, 0, 255), 2)
    return frame


def detectionBLUE(frame):
    """ В качестве аргумента функция принимает кадр, переводит в цветовой формат hsv,
    накладывает маску только синего цвета, сглаживает области и находит контуры.
    Цикл оставляет контуры, подходящие по размеру, и отрисовывает их.
    Функция возвращает кадр, с нарисованными контурами"""
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_mask = cv.inRange(frame_hsv, (44, 134, 92), (255, 255, 255))
    frame_dilate = cv.dilate(frame_mask, None, iterations=2)
    contours, hierarchy = cv.findContours(frame_dilate.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    sort = []
    for i in contours:
        area = cv.contourArea(i)

        if 400 < area < 1500:  # можно регулировать дальность
            sort.append(i)

    cv.drawContours(frame, sort, -1, (0, 0, 255), 2)
    return frame

help(detectionRED)
