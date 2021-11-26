'''
数学公式库，数学方法库
author:pgcai

function:
1. sigmoid
2. tanh
3. relu
4. prelu
5. 求二维数组均值
6. 求二维数组方差
7. 二维数组标准化
'''
import numpy as np

# sigmoid
def sigmoid(x):
    return 1./(1 + np.exp(-x))


# tanh
def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# relu
def relu(x):
    return 0 if x<=0 else x

# prelu
def prelu(x, a=0.25):
    return x if x>0 else a*x

def mean(nlist):
    # nlist = np.array(nlist).flatten()
    return np.mean(nlist)

# 方差
def var(nlist):
    return np.var(nlist)

# 标准差
def std(nlist):
    return np.std(nlist)

# 归一化
def normalization(nlist):
    min = np.min(nlist)
    numrange = np.max(nlist) - min
    return (nlist - min) / numrange


# 标准化
def standardization(nlist):
    return (nlist - mean(nlist)) / std(nlist)

# 指定均值标准差标准化
def sta_mean_std(nlist, mean, std):
    return (nlist - mean) / std


def euclidean_distance(a, b):
    '''
    计算两向量的欧氏距离
    '''
    if len(a)!=len(b):
        print("please input matrix a, b and len(a)==len(b)")
    vector1 = np.mat(a)
    vector2 = np.mat(b)
    # print (np.sqrt((vector1-vector2)*(vector1-vector2).T))
    return np.asarray(np.sqrt((vector1-vector2)*(vector1-vector2).T))[0][0]


def vectorial_resultant(a, b):
    '''
    计算ab两向量合向量
    '''
    return np.array(b)+np.array(a)


def vector_angle(a, b):
    '''
    计算点位a指向点位b的矢量\n
    且各维度平方和为1
    '''
    c = np.array(b) - np.array(a)
    return c/np.sqrt(np.sum(c*c))

def linear_equation_in_2unknowns(a, b, c):
    '''
    解二元一次方程
    '''
    gen = np.sqrt(b*b - 4*a*c)
    x1 = (-b + gen)/(2.*a)
    x2 = (-b - gen)/(2.*a)
    print(x1, x2)
    return [x1, x2]


if __name__=='__main__':
    # print(str(relu(-1)))
    # print(str(relu(999)))
    # a = [4, 2, 35, 4, 325, 6, 1, 345, 54, 4, 554, 6, 1, 325, 78, 4, 55, 676]
    # print(mean(a))
    # print(var(a))
    # print(std(a))
    # b = [[[4, 2], [35, 4], [325,6]],
    # [[1, 345], [54, 4], [554,6]],
    # [[1, 325], [78, 4], [55,676]]]
    # print(mean(b))
    # print(var(b))
    # print(std(b))

    # print(standardization(a))
    # print(standardization(b))

    x = [1,2,3,1,2,3,1,2,3,1,2,3]
    y = [10,23,35,11,24,23,41,12,34,1237,72,53]
    print(euclidean_distance(x,y))

    print(vectorial_resultant(x, y))

    linear_equation_in_2unknowns(4.9, 1000, -999)



