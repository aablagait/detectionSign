from Detection import detectionVIDEO as dtVIDEO
from Detection import detectionIMAGE as dtIMAGE
import cv2 as cv
from name import temp_name
from assemble import conveyer

file = 'database/images/10.png'
image = 'database/ts/00198.jpg'
dtIMAGE(file)


# video = 'static/traffic.mp4'
# dtVIDEO(video)
#
# conveyer('database/images/')

