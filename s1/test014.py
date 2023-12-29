# 鼠标绘图，按下l
import cv2
import numpy as np

curshape = 0
startpos = (0, 0)

img = np.zeros((480, 640, 3), np.uint8)

# 创建窗口
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    global startpos
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if curshape == 0:
            cv2.line(img, startpos, (x, y), (0, 0, 255))
        elif curshape == 1:
            cv2.rectangle(img, startpos, (x, y), (0, 255, 0))
            print('-------')
        elif curshape == 2:
            a = (x - startpos[0])
            b = (x - startpos[1])
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv2.circle(img, startpos, r, (0, 0, 255))


# 设置鼠标回调函数
cv2.setMouseCallback('mouse', mouse_callback)

while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        curshape = 0
    elif key == ord('r'):  # rectangle
        curshape = 1
    elif key == ord('c'):  # circle
        curshape = 2
cv2.destroyAllWindows()
