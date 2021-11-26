'''
excel读写及特殊操作工具箱

function:
1. 读取csv文件返回列表
2. 读取excel文件返回列表
3. 将列表写入到excel
'''
import csv
import pandas as pd

# 读取csv文件返回列表
def read_csv(file_path):
    temp=pd.read_csv(file_path, delimiter=',')      # 比numpy的读取方式好太多，真是术业有专攻。
    return temp.values

# 读取excel文件返回列表
def read_exl(file_path):
    data = pd.read_excel(file_path)

    # print(data.head(3))     # 打印前3行数据  
    # print(data['姓名'])     # 根据列名，打印某一列数据  
    # print(data.columns.tolist())    # 查看所有字段
    # print(data.loc[3])          # 只显示第三行
    # print(data[["姓名", "性别"]])       # # 打印多个列数据，需要双层[[]]

    return data.values

def write2exl(file_path, wlist=[]):
    '''
    将列表写入到excel
    '''
    dic = {'xxx':[1,2,3],
    'yyy':[4,5,6]}
    df = pd.DataFrame(dic)
    df.to_excel('file_path')


if __name__=='__main__':
    fpath = "./example/test.csv"
    fpath2 = "./example/excel.xlsx"
    fpath3 = "./example/data/2011.txt"
    fpath4 = "./example/write.xlsx"
    t = read_csv(fpath)
    print(t)
    x = read_exl(fpath2)
    print(x)
    write2exl(fpath4, [[1,2,3],[4,5,6]])