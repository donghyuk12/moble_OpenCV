#0301.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
#img = np.ones((512,512,3), np.uint8) * 255
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#img = np.zeros((512,512, 3), np.uint8) # Black 배경
pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)
#cv2.imshow('img', img)
#cv2.waitKey()
#cv2.destroyAllWindows()

#==================================================
imageFile = ('./data/Lena.png')
img1 = cv2.imread(imageFile)
cv2.rectangle(img1, pt1, pt2, (0, 0, 255), 5)
cv2.imwrite('./data/squarelena.png',img1,[cv2.IMWRITE_JPEG_QUALITY, 2])

imageFile = ('./data/squarelena.png')
img2 = cv2.imread(imageFile)
cv2.imshow('Lena', img2)
cv2.waitKey()
cv2.destroyAllWindows()
