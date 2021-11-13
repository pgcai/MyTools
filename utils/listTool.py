'''
方便操作关于列表的操作。
实现些numpy不便使用的操作

function:
1. 返回你想要的列
'''
import numpy as np
from txtTool import *

'''
一些较为基础的函数，重新调用意义不大
np.save(path,arr)
存：save()　　取：load()
'''

# 1. 返回你想要的列
# alist为原列表, colname为你想要的列的列表，默认为0
def get_iwant_col(alist=[["!!!原列表为空"]], colname=[0]):
    alist = np.array(alist)
    blist = []
    for i in colname:
        blist.append(alist[:,i])
    return blist
    







if __name__=='__main__':
    print("Welcome to MyTools!")
    txtPath3 = "./example/data/2011.txt"
    a = txt_read_2dim(txtPath3)
    print(a)
    b = get_iwant_col(a, [0,1])
    print(b[0])
