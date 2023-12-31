# OpenCV 绘图

## 直线

`line(img,起始点,结束点,颜色...)`，还可以设置线宽、线型(数字越大越平滑，取值-1，4，8，16)等，shift，坐标比例缩放。坐标格式(x,y)

## 矩形
cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

- img：要画的圆所在的矩形或图像
- pt1：矩形左上角的点
- pt2：矩形右下角的点
- color：线条颜色，如 (0, 0, 255) 红色，BGR
- thickness：线条宽度
- lineType：
    - 8 (or omitted) ： 8-connected line
    - 4：4-connected line
    - CV_AA - antialiased line
shift：坐标点小数点位数

## 圆

cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])

- img：要画的圆所在的矩形或图像
- center：圆心坐标，如 (100, 100)
- radius：半径，如 10
- color：圆边框颜色，如 (0, 0, 255) 红色，BGR
- thickness：正值表示圆边框宽度. 负值表示画一个填充圆形
- lineType：圆边框线型，可为 0，4，8
- shift：圆心坐标和半径的小数点位数

## 椭圆

`ellipse(img,中心点,长宽的一半,角度,从哪个角度开始,到哪个角度结束,颜色,填充)`，

## 多边形

`polylines(img, 点集,是否闭环,颜色)`，点集必须是32位的,np.int32
`fillPoly(img,点集,颜色)`，填充颜色

## 文本

`putText(img,字符串，起始点，字体，字号...)`，

## 



