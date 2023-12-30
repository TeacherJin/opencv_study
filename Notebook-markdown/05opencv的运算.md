# OpenCV中图像的运算

## 图像相加

cv2.add(img1,img2)
会提高亮度

## 图像相减

cv2.subtract(img1,img2)  ,img1-img2
会降低亮度

## 图像相乘和相除

相乘：cv2.multiply(img1,img2)
相除：cv2.divide(img1,img2)

## 图像融合

cv2.addWeighted(img1,alpha,img2,beta,gamma)，alpha表示img1的权重，beta表示img2的权重，alpha+beta应该为1,gamma为静态权重，所有图像都要加上gamma值
img1和img1的大小属性必须一样