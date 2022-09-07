# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np

cap = cv2.VideoCapture('./data/vtest.avi') # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('./data/test09061.mp4',fourcc, 20.0, frame_size)
src2 = cv2.imread('./data/opencv_logo.png')
cv2.imshow('src2',  src2)

while True:
    retval, frame = cap.read()
    if not retval:
        break
#1
    rows,cols,channels = src2.shape
    roi = frame[0:rows, 0:cols]

#2
    gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    

#3
    src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
    cv2.imshow('src1_bg',  src1_bg)

    #4
    src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
    cv2.imshow('src2_fg',  src2_fg)

    #5
    ##dst = cv2.add(src1_bg, src2_fg)
    dst = cv2.bitwise_or(src1_bg, src2_fg)
    cv2.imshow('dst',  dst)

#6
    frame[0:rows, 0:cols] = dst
    out1.write(frame)
    cv2.imshow('result',frame)
    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
out1.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
