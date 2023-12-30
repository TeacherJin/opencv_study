import cv2
import numpy as np

robot=cv2.imread('robot-1.jpg')
# 图的加法运算就是矩阵的加法运算，因此加法运算的两张图必须大小相等
# img的所有值均为100
img=np.ones(robot.shape,np.uint8)*2
# img=np.ones((1200,1920,3),np.uint8)
# 给图加上了白色，亮度会提高
result=cv2.add(robot,img)
orig_1= cv2.divide(result,img)
cv2.imshow('robot',robot)
cv2.imshow('result',result)
cv2.imshow('orig_1',orig_1)
cv2.waitKey(0)
