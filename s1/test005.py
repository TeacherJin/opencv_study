# 鼠标操作
import cv2
import numpy as np

# 自定义回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event,x,y,flags,userdata)

# mousu_callback(1,100,100,16,'666')
# 创建窗口
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,480)

# 设置鼠标回调
cv2.setMouseCallback('mouse', mouse_callback, '123')

# 显示窗口
img=np.zeros((480,640,3),np.uint8)
while True:
    cv2.imshow('mouse',img)
    key=cv2.waitKey(10)
    if key & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()