# 引入opencv
import cv2

# 创建窗口
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
# 设置窗口大小
cv2.resizeWindow('new', 400, 400)
# 显示窗口
cv2.imshow('new', 0)
# 让窗口停留。返回值是按下的键盘的按键
key = cv2.waitKey(0)
# 按下 q 键时，退出
if key == 'q':
    exit()
# 销毁窗口，释放资源
cv2.destroyAllWindows()
