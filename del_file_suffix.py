# -*- code:utf-8 -*-
"""
@file: del_file_suffix
@desc: 删除指定后缀的文件
@example: 文件夹中有jpg格式的原始图片和png格式的分割图片，去掉jpg格式的分割图片
"""
import os
import argparse


def arg_parser():
    parser = argparse.ArgumentParser('code by rbj')
    # 文件夹路径
    parser.add_argument('--filepath', type=str,
                        default="./root/image",
                        help="path_to_folder")
    # 文件后缀
    parser.add_argument('--specified_suffix', type=str,
                        default="jpg",
                        help="specified_suffix")
    # 原网页中是args = parser.parse_args()会报错，改成这个以后解决了
    args = parser.parse_args(args=[])
    return args


def del_file(filepath, specified_suffix):
    files = os.listdir(filepath)
    for file in files:
        if '.' in file:
            suffix = file.split('.')[-1]
            # 指定删除后缀名的文件
            if suffix == specified_suffix:
                os.remove(os.path.join(filepath, file))


if __name__ == '__main__':
    args = arg_parser()
    file_path = args.filepath
    specified_suffix = args.specified_suffix
    del_file(file_path, specified_suffix)
