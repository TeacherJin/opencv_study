# 测试numpy
import numpy as np
import cv2

# 定义一个一维数组
a = np.array([1, 2, 3])
# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])

# 定义zeros矩阵，元素都是0,ones函数类似，元素都是1
c = np.zeros((4, 6, 3), np.uint8)
d = np.ones((4, 6, 3), np.uint8)
e= np.full((8,8,3),255,np.uint8)
# 单元矩阵，正方形矩阵
f=np.identity(8,np.uint8)
# eye定义指定长宽的矩阵,k表示从第几列开始出现1,默认为0
h=np.eye(5,8,k=3)
# print(h)

img=np.zeros((480,640,3),np.uint8)
count=0
# 画一条竖线，白色
while count<200:
    # 画红线，因为是bgr模式，r的通道数是2,b是0,g是1
    # 也可以写作，img[count,100]=[0,0,255]
    img[count,100,2]=255
    count+=1

# 提取子矩阵
roi=img[200:400,200:300]
# 赋值,该部分全为红色，也可以写作roi[:]，roi[:,10]表示所有x为10的元素
roi[:,:]=[0,0,255]
# 子矩阵的一部分改为绿色，超出部分忽略
roi[10:200,10:200]=[0,255,0]


cv2.imshow('img',img)
key=cv2.waitKey(0)
if key&0xFF ==ord('q'):
    cv2.destroyAllWindows()