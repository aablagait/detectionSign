import cv2 as cv
from functions import detectionRED as dtRED, detectionBLUE as dtBLUE, detectionGREEN as dtGREEN
from functions import detectionGREY as dtGREY
from name import unique_name




def detectionVIDEO(video_name):
    """ Функция принимает в качестве аргумента название видео. Каждый кадр передает в функции
    отрисовывания контуров и возвращает кадр с нарисованными контурами.
    Для выхода нажмите кнопку "Esc". """
    video = cv.VideoCapture(video_name)
    while True:
        ret, frame = video.read()
        # frame = dtRED(frame)
        frame, sort = dtBLUE(frame)
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
    print(type(image))
    cadr = cv.imread(image_name)
    spisok = []
    frame, sort = dtBLUE(image, spisok)
    frame, sort = dtRED(frame, sort)
    frame, sort = dtGREEN(frame, sort)
    frame, sort = dtGREY(frame, sort)

    while True:
        cv.drawContours(frame, sort, -1, (0, 234, 135), 2)
        cv.imshow('frame', frame)

        if cv.waitKey(1) == 27:
            break

    return frame

