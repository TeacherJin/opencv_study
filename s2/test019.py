# 图像缩放

# import warnings
# warnings.filterwarnings('ignore')

import cv2
# import numpy as np
# import sys
# for m in sys.modules:
#     print('模块名：',m,'，模块来源：',sys.modules[m])
robot=cv2.imread('robot-2.jpg')
new_robot=cv2.resize(robot,None,fx=0.4,fy=0.4)
# cv2.imwrite('robot-2.jpg',new_robot)
filp1=cv2.flip(robot,-1)
# cv2.imshow('new_robot',new_robot)
cv2.imshow('filp1',filp1)
cv2.waitKey(0)