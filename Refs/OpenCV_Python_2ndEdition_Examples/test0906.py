# 0210.py
import cv2
import PIL

cap = cv2.VideoCapture('./data/vtest.avi') # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter('./data/test09061.mp4',fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/test09062.mp4',fourcc, 20.0, frame_size)

while True:
    retval, frame = cap.read()
    if not retval:
        break   
    
    imageFile = './data/llena.jpg'
    img2 = cv2.imread(imageFile)
    resize_img2 = cv2.resize(img2, (100, 100))
    img2 = resize_img2
    rows, cols, channels = img2.shape
    roi = frame[50:rows+50,50:cols+50]
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_TRUNC)
    mask_inv = cv2.bitwise_not(mask)
    frame_bg = cv2.bitwise_and(roi, roi, mask=mask)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    dst = cv2.bitwise_or(frame_bg, img2_fg)
    
    frame[50:rows+50,50:cols+50] = dst
    
    out1.write(frame)
    cv2.imshow('frame',frame) 
    
    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
out1.release()
cv2.waitKeyEx()
cv2.destroyAllWindows()
