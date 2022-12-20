from techniques import *
# read and view image using opencv

import cv2
img = cv2.imread('images/image.png')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

<<<<<<< HEAD

new_img = image_segmentation(img,100)
=======
new_img = gray_scale(img)
>>>>>>> 97a4eb84a29ebccf13185af44d7de74a12bb5aae
cv2.imshow('gray scale',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



