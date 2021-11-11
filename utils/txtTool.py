'''
操作txt文件的工具箱
author:pgcai

function:
1. 打开txt文件并返回全部内容
2. 以列表形式返回txt中的内容/并去掉回车‘\n’
3. 以列表形式返回txt中的内容/并去掉回车‘\n’/并将他们都转化为float类型
4. 对txt文件写入指定字符串str
5. 对txt文件增添写入指定字符串str
6. “新建”txt文件写入一个数组/"一个元素一行"
7. “对原有” txt文件写入一个数组 "一个元素一行"
8. 两个txt文件 拼接
9. 


模式    可做操作    若文件不存在    是否覆盖
r       只能读         报错         -
r+      可读可写        报错        是
w       只能写          创建        是
w+      可读可写        创建        是
a       只能写          创建        否，追加写
a+      可读可写        创建        否，追加写
'''
import os

'''
读取
'''
# 打开txt文件并返回全部内容
def txtRead(file_path):
    with open(file_path,"r") as f:  #设置文件对象
        str = f.read()     #将txt文件的所有内容读入到字符串str中
    return str

# 以列表形式返回txt中的内容 去掉回车‘\n’
def txtReadArray(file_path, tList=[]):
    with open(file_path,'r') as f:    #设置文件对象
        tList = f.readlines()
    tList = [i[:-1] for i in tList]
    return tList

# 以列表形式返回txt中的内容 去掉回车‘\n’ 并将他们都转化为float类型
def txtReadNumArray(file_path, tList=[]):
    with open(file_path,'r') as f:    #设置文件对象
        tList = f.readlines()
    tList = [float(i[:-1]) for i in tList]
    return tList


'''
写入
'''
# 对txt文件写入字符串 str
def txtWrite(file_path, str):
    with open(file_path,'w') as f:    #设置文件对象
        f.write(str)        #将字符串写入文件中


# 对txt文件!!增添写入字符串 str
def txtAddWrite(file_path, str):
    with open(file_path,'a') as f:    #设置文件对象
        f.write(str+'\n')        #将字符串写入文件中


# “新建”txt文件写入一个数组 "一个元素一行"
def txtWriteArray(file_path, tList=[]):
    tList = [str(i)+"\n" for i in tList]
    with open(file_path,'w') as f:    #设置文件对象
        f.writelines(tList)
    print("txt ok!")


# “对原有”txt文件写入一个数组 "一个元素一行"
def txtAddWriteArray(file_path, tList=[]):
    tList = [str(i) + "\n" for i in tList]
    with open(file_path,'a') as f:    #设置文件对象
        f.writelines(tList)

# 两个txt文件 拼接
def txtAddtxt(path1, path2):
    list2 = txtReadArray(path2)
    txtAddWriteArray(path1, list2)


if __name__ == '__main__':
    print("Welcome to MyTools!")
    txtPath = "./example/data/test.txt"
    txtPath2 = "./example/data/test2.txt"
    txtAddWrite(txtPath,"95633")
    # txtWriteArray(txtPath,[1212, 452345, 2135123])
    txtWriteArray(txtPath,[1, 2, 3])
    txtWriteArray(txtPath2,[4, 5, 6])
    print(len(txtReadArray(txtPath2)))
    print(txtRead(txtPath))
    
    txtAddtxt(txtPath, txtPath2)






