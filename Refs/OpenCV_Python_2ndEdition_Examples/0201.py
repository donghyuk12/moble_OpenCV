# 0201.py
import cv2
import numpy as np
# from PIL import Image
# import numpy as np
imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0) # cv2.IMREAD_GRAYSCALE

#encode_img = np.fromfile(imageFile, np.uint8)
#img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey()
cv2.destroyAllWindows()

# im = Image.open('./data/lena.jpg')
# size = (256, 256)
# im.thumbnail(size)

# mask_ = np.array(im)
# for i in range(len(mask_)):
#     for j in range(len(mask_[i])):
#         if np.sum(mask_[i][j])<45:
#             for k in range(3):
#                 mask_[i][j][k] = 255
# Image.fromarray(mask_, 'RGB')
# cv2.imwrite('./data/llena.jpg', mask_)
# print(mask_.shape)
