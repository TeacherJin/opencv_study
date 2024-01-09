# 图像平移操作

import cv2
import numpy as np

robot = cv2.imread('robot-1.jpg')
h,w,ch=robot.shape
#M=np.float32([[1,0,100],[0,1,300]])
# M=cv2.getRotationMatrix2D((w/2,h/2),15,0.3)
# 通过函数获取M
src=np.float32([[400,300],[800,300],[400,1100]])
dst=np.float32([[200,400],[800,500],[150,1100]])
M=cv2.getAffineTransform(src,dst)

robot2=cv2.warpAffine(robot,M,(w,h) )

cv2.imshow('robot',robot)
cv2.imshow('robot2',robot2)
cv2.waitKey(0)
