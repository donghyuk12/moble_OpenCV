#0309.py
import numpy as np
import cv2
cap = cv2.VideoCapture('./data/vtest.avi')
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('./data/record0.mp4',fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/textrecord.mp4',fourcc, 20.0, frame_size)
while True:
    retval, frame = cap.read()
    if not retval:
        break   
    out1.write(frame)
    img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
    text = 'OpenCV Programming'
    org = (75,100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,0,0), 2)      
    out2.write(frame)
    cv2.imshow('text', frame)
    
    key = cv2.waitKey(25)
    if key == 27:
        break
# img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# text = 'OpenCV Programming'
# org = (75,100)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,text, org, font, 1, (255,0,0), 2)

# size, baseLine = cv2.getTextSize(text, font, 1, 2)
# #print('size=', size)
# #print('baseLine=', baseLine)
# cv2.rectangle(img, org, (org[0]+size[0], org[1]-size[1]), (0, 0, 255))
# cv2.circle(img, org, 3, (0, 255,0), 2)

# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
cap.release()
out1.release()
cv2.destroyAllWindows()
