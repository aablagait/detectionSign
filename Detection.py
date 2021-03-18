import cv2 as cv
from functions import detectionRED as dtRED, detectionBLUE as dtBLUE


def detectionSign(file_name):
    """ Функция принимает в качестве аргумента название видео. Каждый кадр передает в функции
    отрисовывания контуров и возвращает кадр с нарисованными контурами.
    Для выхода нажмите кнопку "Esc". """
    video = cv.VideoCapture(file_name)
    while True:
        ret, frame = video.read()
        frame = dtBLUE(frame)
        frame = dtRED(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:
            break
    video.release()
    cv.destroyAllWindows()
    return frame


