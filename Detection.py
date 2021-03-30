import cv2 as cv
from functions import detectionRED as dtRED, detectionBLUE as dtBLUE, detectionBLUEYUV as dtYUV


def detectionVIDEO(video_name):
    """ Функция принимает в качестве аргумента название видео. Каждый кадр передает в функции
    отрисовывания контуров и возвращает кадр с нарисованными контурами.
    Для выхода нажмите кнопку "Esc". """
    video = cv.VideoCapture(video_name)
    while True:
        ret, frame = video.read()
        # frame = dtRED(frame)
        frame = dtBLUE(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:
            break
    video.release()
    cv.destroyAllWindows()
    return frame


def detectionIMAGE(image_name):
    """ Функция принимает в качестве аргумента название изображения. Передает в функции
    отрисовывания контуров и возвращает изображение с нарисованными контурами.
    Для выхода нажмите кнопку "Esc". """
    image = cv.imread(image_name)
    while True:
        frame = dtBLUE(image)
        # frame = dtRED(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:
            break
    return frame

