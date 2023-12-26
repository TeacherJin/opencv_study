# mat的属性
import cv2
import numpy as np

img=cv2.imread('Auto-013.jpg')
# shape属性，包含高度，宽度和通道数
print(img.shape)
# size属性，占用多大空间，高度*宽度*通道数
print(img.size)
# 图像中每个元素的位深
print(img.dtype)