# 添加水印
import cv2
import numpy as np

# 引入图片
robot=cv2.imread('robot-1.jpg')
# 创建logo
logo=np.zeros((200,200,3),np.uint8)
mask=np.zeros((200,200),np.uint8)
# 绘制logo
logo[20:120,20:120]=[0,0,255]
logo[80:180,80:180]=[0,255,0]

mask[20:120,20:120]=255
mask[80:180,80:180]=255

# 对mask求反
m=cv2.bitwise_not(mask)
# 选择添加logo的位置
roi=robot[0:200,0:200]
# 与m进行与操作
tmp=cv2.bitwise_and(roi,roi,m)
dst=cv2.add(tmp,logo)
# 计算图片在什么地方添加logo
robot[0:200,0:200]=dst
# 利用add把logo和图片叠加到一起

cv2.imshow('logo',logo)
cv2.imshow('tmp',tmp)
cv2.imshow('dst',dst)
cv2.imshow('robot',robot)
cv2.waitKey(0)