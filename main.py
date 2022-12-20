from techniques import *
# read and view image using opencv

import cv2
img = cv2.imread('images/image.png')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


new_img = erosion(img,5)

cv2.imshow('gray scale',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




