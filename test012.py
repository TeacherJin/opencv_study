# 画直线
import cv2
import numpy as np

img=np.zeros((480,640,3),np.uint8)
# 画线
cv2.line(img,(10,20),(300,400),(0,0,255),5,16)
cv2.line(img,(10,40),(300,440),(0,0,255),5,2)
cv2.imshow('draw',img)

cv2.waitKey(0)