# 图像旋转
import cv2
import numpy as np
robot2=cv2.imread('robot-2.jpg')
robot3=cv2.rotate(robot2,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('robot2',robot2)
cv2.imshow('robot3',robot3)

cv2.waitKey(0)