import cv2 as cv

# 打开视频文件
video_file = "input.mp4"

# 读取视频文件
video = cv.VideoCapture(video_file)

# 检查视频是否成功打开
if not video.isOpened():
    print("无法打开视频文件")
    exit()

while True:
    # 读取视频帧
    ret, frame = video.read()

    # 如果没有成功读取帧，说明已经到了视频的末尾，退出循环
    if not ret:
        break

    # 在窗口中显示视频帧（可选）
    cv.imshow('camera', frame)

    # 按'q'键退出循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv.destroyAllWindows()
