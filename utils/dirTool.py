'''
获取文件夹下所有图片的路径
author:pgcai
function:
1. get_file(file_path, file_end=('.png', '.jpg', '.jpeg'))      获取指定文件夹下指定后缀文件/不包含子文件夹
2. get_numfile(file_path, file_end=('.png', '.jpg', '.jpeg'))   获取指定文件夹下指定后缀文件/不包含子文件夹//文件名需要为number/排序
3. get_file_sub(file_path, filelist=[], file_end=('.png', '.jpg'))      获取指定文件夹下指定后缀文件/包含子目录
4. get_numfile_sub(file_path, filelist=[], file_end=('.png', '.jpg'))   获取指定文件夹下指定后缀文件/包含子目录/文件名需要为number/排序
5. new_folder(dirpath)  根据当前时间新建文件夹
6. change_suffix(dirpath, file_end=['.png','.jpg'], end_new='')   改变文件夹下指定后缀文件的后缀更改为自定义后缀
7. change_name(dirpath, file_end=['.png','.jpg'], name_add='')    文件名后增加字符串（批量修改文件名）
'''
import sys
sys.path.append(r'./utils')      # 为了能找到自写函数

import os
import re
from dateTool import *


def get_file(file_path, file_end=('.png', '.jpg', '.jpeg')):
    '''
    获取指定文件夹下指定后缀文件,不包含子文件夹
    (文件夹路径, 后缀名)
    '''
    filelist = []
    for parent, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            if filename.lower().endswith(file_end):
                filelist.append(os.path.join(parent, filename))
        return filelist

def get_numfile(file_path, file_end=('.png', '.jpg', '.jpeg')):
    '''
    获取指定文件夹下指定后缀文件,不包含子文件夹     数字文件排序
    (文件夹路径, 后缀名)
    '''
    filelist = []
    for parent, dirnames, filenames in os.walk(file_path):
        filenames.sort(key=lambda x:int(x[:-4]))  # 按文件名排序 
        for filename in filenames:
            if filename.lower().endswith(file_end):
                filelist.append(os.path.join(parent, filename))
        return filelist



def get_file_sub(file_path, filelist=[], file_end=('.png', '.jpg')):
    '''
    获取指定文件夹下指定后缀文件 包含子目录
    '''
    print('\r--------正在统计文件夹下指定后缀文件路径信息--------', end="")
    for parent, dirnames, filenames in os.walk(file_path):
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            filelist.extend(get_file_sub(os.path.join(parent, dirname), [], file_end=file_end))
            # print(filelist)
        print(filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                filelist.append(os.path.join(parent, filename))
        return filelist

def get_numfile_sub(file_path, filelist=[], file_end=('.png', '.jpg')):
    '''
    获取指定文件夹下指定后缀文件 包含子目录 文件名需要为 number 便于排序
    '''
    print('\r--------正在统计文件夹下指定后缀文件路径信息--------', end="")
    for parent, dirnames, filenames in os.walk(file_path):
        dirnames.sort() # 按文件夹名排序
        # print("--------------------------------")
        # print(dirnames)
        # print("--------------------------------")
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            filelist.extend(get_numfile_sub(os.path.join(parent, dirname), [], file_end=file_end))
            # print(filelist)
            
        # print("old",filenames)
        filenames.sort(key=lambda x:int(x[:-4]))  # 按文件名排序 
        # print("new",filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                filelist.append(os.path.join(parent, filename))
        return filelist

def new_folder(dirpath):
    '''
    根据当前时间(年月日时分秒)新建文件夹
    '''
    timeString = getDateYMDHMS()
    makePath = dirpath + '/' + timeString
    folder = os.path.exists(makePath)

    if not folder:
        os.makedirs(makePath)
        print("make dir success!")
        return(makePath)
    else:
        print("folder already exists!")
        return(makePath)

def change_suffix(dirpath, file_end=['.png','.jpg'], end_new=''):
    '''
    改变文件夹下指定后缀文件的后缀更改为自定义后缀
    '''
    for i in file_end:
        print('i = ',i)
        # break
        print(len(i))
        dir_list = get_file(rename_path, i)
        for j in dir_list:
            os.rename(j, j[:-len(i)] + end_new)

def change_name(dirpath, file_end=['.png','.jpg'], name_add=''):
    '''
    文件名后增加字符串（批量修改文件名）
    '''
    for i in file_end:
        print('i = ',i)
        # break
        print(len(i))
        dir_list = get_file(rename_path, i)
        for j in dir_list:
            os.rename(j, j[:-len(i)] + name_add + j[-len(i):])
            


if __name__ == '__main__':
    print("Welcome to MyTools!")

    trainpath='./example'
    # 获取文件夹包含子目录下后缀为.jpg的文件
    dir_list = get_file_sub(trainpath, file_end=('.jpg'))
    print(dir_list)
    print(len(dir_list))

    # 获取文件夹包含子目录下后缀为.jpg、.png的文件
    print(get_file("./img",('png','jpg')))

    # 根据当前时间(年月日时分秒)新建文件夹
    # newPath = new_folder("./example")

    rename_path = "E:/DataSet/fire_smoke/FireDateset/fire_dataset/fire_images"
    change_suffix(rename_path,['.png'], '.jpg')




