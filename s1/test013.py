# 绘制椭圆

import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)
# 绘制矩形
cv2.rectangle(img, (10, 10), (100, 120), (200, 0, 0))
# 绘制圆形
cv2.circle(img, (150, 150), 66, (0, 255, 0))
# 绘制椭圆
cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 180, (0, 0, 255), -1)
# 绘制多边形
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
cv2.polylines(img, [pts],True,(0,0,255))
cv2.fillPoly(img,[pts],[150,100,150])
# 绘制文本
cv2.putText(img,'hello world,白日依山尽',(10,400),cv2.FONT_HERSHEY_TRIPLEX,3,(255,0,0))
cv2.imshow('img', img)
cv2.waitKey(0)
