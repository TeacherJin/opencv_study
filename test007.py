# 色彩空间转换
import cv2

def callback():
    pass

cv2.namedWindow('color', cv2.WINDOW_NORMAL)
img=cv2.imread('/home/vk/Pictures/desktop/10872.jpg')
colorspace=[cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,
            cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV_FULL,
            cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor','color',0,len(colorspace)-1,callback)
while True:
    index=cv2.getTrackbarPos('curcolor','color')
    # 颜色空间转换挨批
    cvt_img=cv2.cvtColor(img,colorspace[index])
    cv2.imshow('color',cvt_img)
    key=cv2.waitKey(10)
    if key & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()