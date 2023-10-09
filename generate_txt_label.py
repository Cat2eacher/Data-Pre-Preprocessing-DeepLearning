# -*- code:utf-8 -*-
"""
@file: generate txt label
@desc: 生成对应train,valid,test数据集的txt标签文件
       其中每一行表示一张照片的路径和对应的类别索引。这些列件在训练和预测过程中可以被使用
@notice: 必须先运行split_data.py文件，划分出train,valid,test的新数据集文件夹
@result: 在对应数据集文件夹下产生train.txt, valid.txt, (test.txt) 文件
"""

import os

'''
/****************************************************/
数据集文件夹下有一个txt文件class_name.txt
存放所有类别信息
/****************************************************/
'''


def get_classes(class_txt_path):
    """
    读取一个包含类别名称的文件，并返回类别列表和类别数量
    :param class_txt_path: 给定的文件路径
    :return:
    """
    with open(class_txt_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)


'''
/****************************************************/
生成对应train,valid,test数据集的txt标签文件
/****************************************************/
'''


def txt_label(dataset_path, datasets, classes):
    for set in datasets:
        # 打开对应数据集txt文件
        txt_file = open(dataset_path + '/' + set + '.txt', 'w')
        # 构建当前集合的数据集路径
        set_path = os.path.join(dataset_path, set)
        # 获取当前数据集路径下的所有类别文件夹名称，并遍历每个类别
        classes_name = os.listdir(set_path)
        for class_name in classes_name:
            # 如果当前类别不在类别列表 classes 中，跳过当前类别
            if class_name not in classes:
                continue
            # 获取当前类别的索引 cls_id，通过 classes.index(type_name) 获取
            cls_id = classes.index(class_name)
            # 构建当前类别的图像路径 images_path，通过 os.path.join 将当前数据集路径和类别名称进行拼接
            images_path = os.path.join(set_path, class_name)
            # 获取当前类别路径下的所有图像文件名称，并遍历
            images_list = os.listdir(images_path)
            for image in images_list:
                _, postfix = os.path.splitext(image)
                if postfix not in ['.jpg', '.png', '.jpeg']:
                    continue
                image_path = os.path.relpath(os.path.join(images_path, image), dataset_path)
                txt_file.write(str(cls_id) + ";" + '%s' % (image_path))
                txt_file.write('\n')
        txt_file.close()


if __name__ == "__main__":
    # -------------------------------------------------------------------#
    #   class_name_path     保存类别标签的txt文件，与数据集相关
    # -------------------------------------------------------------------#
    class_name_path = './dataset/public/Magnetic-Tile-Defect/dataset_split/class_name.txt'
    # -------------------------------------------------------#
    #   dataset_path       数据集位置
    # -------------------------------------------------------#
    dataset_path = "./dataset/public/Magnetic-Tile-Defect/dataset_split"
    # -------------------------------------------------------#
    #   sets = ["train", "valid"]
    # -------------------------------------------------------#
    sets = ["train", "valid", "test"]
    # -------------------------------------------------------#
    #   CLASSES
    # -------------------------------------------------------#
    classes, _ = get_classes(class_name_path)

    txt_label(dataset_path, sets, classes)
