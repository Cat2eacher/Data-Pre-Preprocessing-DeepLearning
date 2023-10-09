# -*- code:utf-8 -*-
"""
@file: split_data
@desc: 划分数据集
@example: 只有一个数据集文件夹，数据集文件夹下每个类别有子文件夹。
          但并未划分训练集和测试集
@result: 创建一个新数据集文件夹，新数据集文件夹下有train,valid,test三个文件夹
"""

import os
import random
import shutil


# -------------------------------------------------------#
#   make_dir
# -------------------------------------------------------#
def make_dir(path):
    if os.path.exists(path):
        os.removedirs(path)
        os.makedirs(path)
    else:
        os.makedirs(path)


# -------------------------------------------------------#
#   split_data 数据集划分
# -------------------------------------------------------#
def split_data(data_path, save_path, train_rate, val_rate, test_rate):
    data_path = data_path  # 原始数据集位置
    save_path = save_path  # 划分训练集和验证集所处的位置

    class_names = []
    for cla in os.listdir(data_path):
        class_names.append(cla)
    num_classes = len(class_names)

    # 创建对应文件夹
    for cla in class_names:
        # make_dir(save_path + '/' + 'train' + '/' + cla)
        make_dir(os.path.join(save_path, "train", cla))
        # make_dir(save_path + '/' + 'valid' + '/' + cla)
        make_dir(os.path.join(save_path, "valid", cla))
        # make_dir(save_path + '/' + 'test' + '/' + cla)
        make_dir(os.path.join(save_path, "test", cla))

    index = 0
    for cla in class_names:
        image_list = []
        # image_list = os.listdir(os.path.join(data_path, cla))
        for image in os.listdir(os.path.join(data_path, cla)):
            image_list.append(image)
        num = len(image_list)
        random.shuffle(image_list)
        train_images = image_list[0:int(train_rate * num)]  # 注意左闭右开
        val_images = image_list[int(train_rate * num):int((train_rate + val_rate) * num)]  # 注意左闭右开
        test_images = image_list[int((train_rate + val_rate) * num):]

        for image in train_images:
            # old_path = data_path + '/' + cla + '/' + image
            old_path = os.path.join(data_path, cla, image)
            # new_path = save_path + '/' + 'train' + '/' + cla + '/' + image
            new_path = os.path.join(save_path, 'train', cla, image)
            shutil.copy(old_path, new_path)

        for image in val_images:
            # old_path = data_path + '/' + cla + '/' + image
            old_path = os.path.join(data_path, cla, image)
            # new_path = save_path + '/' + 'valid' + '/' + cla + '/' + image
            new_path = os.path.join(save_path, 'valid', cla, image)
            shutil.copy(old_path, new_path)

        for image in test_images:
            # old_path = data_path + '/' + cla + '/' + image
            old_path = os.path.join(data_path, cla, image)
            # new_path = save_path + '/' + 'test' + '/' + cla + '/' + image
            new_path = os.path.join(save_path, 'test', cla, image)
            shutil.copy(old_path, new_path)


if __name__ == '__main__':
    # 保证随机可复现
    random.seed(0)
    data_path = "../dataset/public/Magnetic-Tile-Defect/dataset_classification"
    save_path = "../dataset/public/Magnetic-Tile-Defect/dataset_split"
    split_data(data_path, save_path, train_rate=0.8, val_rate=0.2, test_rate=0.0)
