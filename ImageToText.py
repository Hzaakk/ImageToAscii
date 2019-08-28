import cv2
import numpy as np
import bisect
import os

RESOLUTION = 50 # How many lines of text. Will give an error if too high
SCALE = ' .,-:"»/¤=+*Xc%ZM#@¶'[::-1]
RANGES = [round(255/len(SCALE) * i) for i in range(len(SCALE))]
img = cv2.imread('image.jpg', 0)

pixel_y = img.shape[0] / RESOLUTION
pixel_x = pixel_y * img.shape[0] / img.shape[1]

text = ''

for y in np.arange(0, img.shape[0] - pixel_y, pixel_y):
    for x in np.arange(0, img.shape[1] - pixel_x, pixel_x):
        pixel = img[int(round(y)):int(round(y + pixel_y)), int(round(x)):int(round(x + pixel_x))].mean()
        text += SCALE[bisect.bisect_left(RANGES, pixel - RANGES[1])]
    text += '\n'

with open('text.txt','w') as f:
    f.write(text)

os.system('notepad.exe ' + os.path.realpath('text.txt'))                 
