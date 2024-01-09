# 图像平移操作

import cv2
import numpy as np

robot = cv2.imread('robot-2.jpg')
h,w,ch=robot.shape
# M=np.float32([[1,0,100],[0,1,300]])
# 通过api计算M，中心点是x，y，也就是宽、高
M=cv2.getRotationMatrix2D((w/2,h/2),15,0.3)

robot2=cv2.warpAffine(robot,M,(w,h) )

cv2.imshow('robot',robot)
cv2.imshow('robot2',robot2)
cv2.waitKey(0)
