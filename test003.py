import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('/home/vk/Pictures/desktop/99a.jpg')
# cv2.imshow('img', img)
# key = cv2.waitKey(0)
# if key&0xFF == ord('q'):
#     # 退出
#     cv2.destroyAllWindows()
# elif(key & 0xFF == ord('s')):
#     # 按下s键时保存，但此时程序会退出。按下任何键都会退出，因为不管按下什么键，都不再执行waitKey函数，往下执行，不再等待，所以退出
#     cv2.imwrite('/home/vk/Pictures/123.png',img)

# 想要解决上述问题，可以把这部分代码放到循环中
while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)
    if chr(key) == 'q':
        # 打破循环，退出程序
        break
    elif chr(key) == 's':
        # 按下s键时保存，但此时程序会退出。按下任何键都会退出，因为不管按下什么键，都不再执行waitKey函数，往下执行，不再等待，所以退出
        cv2.imwrite('/home/vk/Pictures/123.png', img)