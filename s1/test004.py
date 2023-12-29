# 通过摄像头视频采集
import cv2

fourcc=cv2.VideoWriter.fourcc(*'mp4v')
# 摄像头为1920*1080，但只能用640*480
vw=cv2.VideoWriter('./out.mp4',fourcc,25,(640,480))
# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
# 获取视频设备，参数也可以是一个视频文件
cap = cv2.VideoCapture(0)
# 判断摄像头是否打开
while cap.isOpened():
    ret, frame = cap.read()
    # 如果读取成功才进行下一步
    if ret:
        cv2.imshow('video', frame)
        # 写数据到多媒体文件
        vw.write(frame)
        # 如果等待时间为0,只显示第一帧，可以改为稍大一点，隔一段时间运行一次
        # 但不能用chr(key)判断了
        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'):
            break
    else:
        break
# 释放VideoCapture
cap.release()
cv2.destroyAllWindows()
vw.release()