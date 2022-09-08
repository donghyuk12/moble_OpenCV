import pafy
import cv2

url = 'https://www.youtube.com/watch?v=433HGrqXk_k'

video = pafy.new(url)
print("title = ", video.title)
best = video.getbest(preftype = 'any')
template = cv2.imread('./data/wony.png')
th, tw = template.shape[:2]
cv2.imshow('testlena', template)

capture = cv2.VideoCapture(best.url)
while True:
    ret,image =capture.read()
    if not ret:
        break
    
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    top_left = maxLoc
    match_val = maxVal
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
    cv2.imshow('webCAM', image)   
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
        

