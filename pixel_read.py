# -*- coding: utf-8 -*-
"""
@file name:pixel_read.py
@desc:获取视频首帧像素值和坐标
"""
import cv2 as cv

'''
/**************************task1**************************/
导入视频文件
/**************************task1**************************/
'''
# ----------------------------------------------------#
#           视频文件读取
# ----------------------------------------------------#
# 打开视频文件
input_video_path = "VIS.mp4"

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


def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        # 清除之前的文本信息
        first_frame_copy[:] = first_frame[:]

        # 获取像素值和坐标
        coordinates = f'({x}, {y})'
        coordinates_info = f'Coord Value: {coordinates}'
        pixel_value = first_frame_copy[y, x]
        pixel_info = f'Pixel Value: {pixel_value}'

        # 添加新的文本信息
        cv.putText(first_frame_copy, coordinates_info, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, color=(255, 255, 255),
                   thickness=2)
        cv.putText(first_frame_copy, pixel_info, (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, color=(255, 255, 255),
                   thickness=2)

        # 更新窗口显示
        cv.imshow(window_name, first_frame_copy)


# 设置鼠标事件回调函数
cv.setMouseCallback(window_name, mouse_callback)
cv.imshow(window_name, first_frame)
cv.waitKey(0)
cv.destroyAllWindows()

# 释放视频对象和关闭窗口
input_video.release()
