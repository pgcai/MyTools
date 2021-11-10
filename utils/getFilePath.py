'''
获取文件夹下所有图片的路径
author:pgcai
'''

import os
import re


'''
获取指定文件夹下指定后缀文件
(文件夹路径, 后缀名)
'''
def get_file(file_path, file_end=('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
    imagelist = []
    for parent, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            if filename.lower().endswith(file_end):
                imagelist.append(os.path.join(parent, filename))
        return imagelist


'''
获取指定文件夹下指定后缀文件 包含子目录
'''

def get_file_sub(file_path, imagelist=[], file_end=('.png', '.jpg')):
    print('\r--------正在统计文件夹下指定后缀文件路径信息--------', end="")
    for parent, dirnames, filenames in os.walk(file_path):
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            imagelist.extend(get_file_sub(os.path.join(parent, dirname), [], file_end=file_end))
            # print(imagelist)
        print(filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                imagelist.append(os.path.join(parent, filename))
        return imagelist

'''
获取指定文件夹下指定后缀文件 包含子目录 文件名需要为number
'''
def get_numfile_sub(file_path, imagelist=[], file_end=('.png', '.jpg')):
    print('\r--------正在统计文件夹下指定后缀文件路径信息--------', end="")
    for parent, dirnames, filenames in os.walk(file_path):
        dirnames.sort() # 按文件夹名排序
        # print("--------------------------------")
        # print(dirnames)
        # print("--------------------------------")
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            imagelist.extend(get_numfile_sub(os.path.join(parent, dirname), [], file_end=file_end))
            # print(imagelist)
            
        # print("old",filenames)
        filenames.sort(key=lambda x:int(x[:-4]))  # 按文件名排序 
        # print("new",filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                imagelist.append(os.path.join(parent, filename))
        return imagelist


if __name__ == '__main__':
    trainpath='./pic'
    
    # 获取文件夹包含子目录下后缀为.jpg的文件
    dir_list = get_file_sub(trainpath, file_end=('.jpg'))
    print(dir_list)
    print(len(dir_list))

    # 获取文件夹包含子目录下后缀为.jpg、.png的文件
    print(get_file("./img",('png','jpg')))




