# -*- coding: utf-8 -*-
"""
@file name:video_crop.py
@desc:对视频进行裁剪
"""
import cv2 as cv
'''
/**************************task1**************************/
导入输入视频文件
指定输出视频文件
/**************************task1**************************/
'''

# ----------------------------------------------------#
#           视频文件读取
# ----------------------------------------------------#
# 打开视频文件
input_video_path = "aa_VIR.mp4"
output_video_path = "output.mp4"

# 读取视频文件
input_video = cv.VideoCapture(input_video_path)

# 检查视频是否成功打开
if not input_video.isOpened():
    print("无法打开视频文件")
    exit()

# ----------------------------------------------------#
#           获取视频的基本信息
# ----------------------------------------------------#
# frame_width = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))
frame_width = int(input_video.get(3))  # 帧宽度
print("视频的宽度为：", frame_width)
# frame_height = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))
frame_height = int(input_video.get(4))  # 帧高度
print("视频的高度为：", frame_height)
# 获取视频的帧数
frame_number = int(input_video.get(cv.CAP_PROP_FRAME_COUNT))
print("视频的帧数为：", frame_number)
# 获取视频的帧率
# frame_rate = input_video.get(cv.CAP_PROP_FPS)
frame_rate = int(input_video.get(5))  # FPS
print("视频的帧率为：", frame_rate)

'''
/**************************task2**************************/
第一帧处理
/**************************task2**************************/
'''
# ----------------------------------------------------#
#           读取第一帧
# ----------------------------------------------------#
ret, first_frame = input_video.read()
# 检查是否成功读取第一帧
if not ret:
    print("无法读取第一帧")
    exit()

# ----------------------------------------------------#
#           设定第一帧显示窗口并设置窗口大小
# ----------------------------------------------------#
# 定义窗口的名称和标志（使用cv2.WINDOW_NORMAL标志，允许调整窗口大小）
window_name = 'First Frame'
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

# 设置窗口的大小
desired_width = 800  # 设置希望的窗口宽度
desired_height = 600  # 设置希望的窗口高度

# 计算图像的纵横比和窗口的纵横比
frame_aspect_ratio = frame_width / frame_height
desired_aspect_ratio = desired_width / desired_height

# 根据纵横比差异调整窗口大小
if frame_aspect_ratio > desired_aspect_ratio:
    new_width = desired_width
    new_height = int(new_width / frame_aspect_ratio)
else:
    new_height = desired_height
    new_width = int(new_height * frame_aspect_ratio)

# 设置窗口的大小
cv.resizeWindow(window_name, new_width, new_height)

# ----------------------------------------------------#
#           定义鼠标事件回调函数
# ----------------------------------------------------#
first_frame_copy = first_frame.copy()
# 定义全局变量
action = 1  # 自定义标志 1：鼠标左键按下时记录位置标志  3：鼠标左键鼠标松开 4：清除图片中的标志
point_start = (0, 0)  # 记录标记起始点
point_end = (0, 0)  # 记录标记终点


# 实现回调函数
def mouse_callback(event, x, y, flags, image):
    global action, point_start, point_end
    if event == cv.EVENT_LBUTTONDOWN and flags == cv.EVENT_FLAG_LBUTTON:  # 当鼠标左键及拖拽时
        # 记录起始位置
        if action == 1:
            action = 2  # 记录到了起点位置就可以，跳到第二部步，等待左键鼠标放开
            point_start = (x, y)  # 记录起点位置
    if event == cv.EVENT_LBUTTONUP:  # 检测到鼠标左键鼠标松开
        point_end = (x, y)  # 记录终点坐标
        action = 3
    if event == cv.EVENT_RBUTTONDOWN:  # 鼠标右键按下标志
        action = 4


# 设置鼠标事件回调函数
cv.setMouseCallback(window_name, mouse_callback)
# 显示第一帧图像
cv.imshow(window_name, first_frame)
while True:
    # 清除之前的文本信息
    first_frame_copy[:] = first_frame[:]
    if action == 3:  # 显示图片
        action = 1
        cv.rectangle(first_frame_copy, point_start, point_end, (0, 255, 0), 2)  # 根据起点坐标和终点坐标绘制矩形框
        print(point_start, point_end)
        cv.imshow(window_name, first_frame_copy)
    if action == 4:  # 鼠标右键按下时清除图片中的标记，其主要思想就是重新读取照片，再重新显示
        point_start = (0, 0)
        point_end = (0, 0)
        action = 1
        cv.imshow(window_name, first_frame)
    key = cv.waitKey(1)  # 这里等待时间不要设置0,不然图片显示不出来
    if key == ord('q'):
        break
cv.destroyAllWindows()

'''
/**************************task3**************************/
视频裁剪
/**************************task3**************************/
'''
# ----------------------------------------------------#
#           创建输出视频对象
# ----------------------------------------------------#
# 如果成功读取第一帧
# 创建输出视频对象，用于保存处理后的视频
# VideoWriter_fourcc为视频编解码器
fourcc = cv.VideoWriter_fourcc(*'mp4v')
x_start = point_start[0]
y_start = point_start[1]
x_end = point_end[0]
y_end = point_end[1]
crop_width = x_end - x_start
crop_height = y_end - y_start
output_video = cv.VideoWriter(output_video_path, fourcc, frame_rate, (crop_width, crop_height))

# ----------------------------------------------------#
#           逐帧生成
# ----------------------------------------------------#
if ret:
    while True:
        # 读取下一帧
        ret, frame = input_video.read()

        # 如果不能读取帧，说明已经到达视频的末尾，退出循环
        if not ret:
            break

        cropped_frame = frame[y_start:y_end, x_start:x_end, :]

        # 将差值帧写入输出视频
        output_video.write(cropped_frame)

    # 释放视频对象
    input_video.release()
    output_video.release()

    print("输出视频已保存")
else:
    print("无法读取第一帧")

# 释放视频对象和关闭窗口
input_video.release()
output_video.release()
