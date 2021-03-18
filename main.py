from Detection import detectionSign as dtSign
import cv2 as cv


file = 'static/traffic.mp4'
cv.imshow('frame', dtSign(file))