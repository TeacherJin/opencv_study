# 绘制椭圆

import cv2
import numpy as np

img=np.zeros((480,640,3),np.uint8)
cv2.ellipse(img,(320,240),(100,50),0,0,180,(0,0,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)