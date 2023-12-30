# 图像融合
import cv2
import numpy as np

back=cv2.imread('./scenery-1.jpg')
robot=cv2.imread('robot-1.jpg')

result=cv2.addWeighted(robot,0.7,back,0.3,0)
cv2.imshow('add2',result)
cv2.waitKey(0)