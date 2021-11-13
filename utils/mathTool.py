'''
数学公式库，数学方法库
author:pgcai

function:

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


if __name__=='__main__':
    print(str(relu(-1)))
    print(str(relu(999)))


















