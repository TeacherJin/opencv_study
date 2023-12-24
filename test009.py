# mat的浅拷贝和深拷贝
import cv2
import numpy

img=cv2.imread('./Auto-013.jpg')
# 浅拷贝
img2=img
# 深拷贝
img3=img.copy()
# 修改img的图像,img2也会随之改变，说明是浅拷贝
img[10:100,10:100]=[0,0,255]
cv2.imshow('img2',img2)
key=cv2.waitKey(0)
if key &0xFF==ord('q'):
    cv2.destroyAllWindows()

