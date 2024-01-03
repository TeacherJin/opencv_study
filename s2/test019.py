# 图像缩放

import cv2
import numpy as np
robot=cv2.imread('robot-1.jpg')
new_robot=cv2.resize(robot,None,fx=0.4,fy=0.4)
# cv2.imwrite('robot-2.jpg',new_robot)
filp1=cv2.flip(robot,-1)
# cv2.imshow('new_robot',new_robot)
cv2.imshow('filp1',filp1)
cv2.waitKey(0)