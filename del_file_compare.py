# -*- code:utf-8 -*-
"""
@file: del_file_compare
@desc: 删除没有对应文件名的文件
@example: yolo数据集一张图片对应一个txt文件，删除一些图片后，部分txt文件没有对应，进行删除
"""
import os
import argparse


def arg_parser():
    parser = argparse.ArgumentParser('删除 YOLO 数据集中没有对应图片的 txt 文件')
    # 图片文件夹的路径
    parser.add_argument('--image_folder', type=str,
                        default="./fire_VOC/images",
                        help="path_to_image_folder")
    # 标注文件夹的路径
    parser.add_argument('--annotation_folder', type=str,
                        default="./fire_VOC/Annotations",
                        help="path_to_annotation_folder")
    # 标注文件类型：xml or txt
    parser.add_argument('--annotation_type', type=str,
                        default="xml",
                        help="type_to_annotation_file")
    # 原网页中是args = parser.parse_args()会报错，改成这个以后解决了
    args = parser.parse_args(args=[])
    return args


if __name__ == '__main__':
    args = arg_parser()
    image_folder = args.image_folder
    annotation_folder = args.annotation_folder
    type = args.annotation_type

    # 获取所有图片文件的文件名（不包括文件扩展名）
    image_filenames = set([os.path.splitext(filename)[0] for filename in os.listdir(image_folder)])

    # 获取所有 annotation 文件的文件名（不包括文件扩展名）
    annotation_filenames = set([os.path.splitext(filename)[0] for filename in os.listdir(annotation_folder)])

    # 找到不匹配的文件名（txt 文件没有对应的图片文件）
    unmatched_txt_files = annotation_filenames - image_filenames

    # 删除不匹配的 txt 文件
    for filename in unmatched_txt_files:
        txt_file_path = os.path.join(annotation_folder, filename + type)
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)

    print(f"Deleted {len(unmatched_txt_files)} unmatched txt files.")
