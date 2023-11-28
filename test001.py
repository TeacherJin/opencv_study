# 测试opencv，打开并显示一张图片文件
import cv2
img=cv2.imread('/home/vk/Pictures/desktop/城市风光/City-140.jpg')

cv2.imshow('img',img)
cv2.waitKey(0)