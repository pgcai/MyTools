'''
img tools
包含图片处理常见工具.
function:
1. 根据路径返回img
2. 根据路径保存图片
3. 画折线图
'''
import sys
sys.path.append(r'./')      # 为了能找到自写函数

import cv2
import matplotlib.pyplot as plt
from utils.txtTool import *

def get_img(getpath):
    img = cv2.imread(getpath)
    return img

def save_img(savepath, img):
    cv2.imwrite(savepath, img)


def plot_line_chart(y1, y2, y3):

    plt.figure(figsize=(20,2))
    plt.title('太阳风速度预测')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('time')  # x轴标题
    plt.ylabel('太阳风速 km/s')  # y轴标题
    plt.plot(y1, color='#800080', label='true', linewidth=1)  # 绘制折线图，添加数据点，设置点的大小
    # plt.plot(y2, color='#00a8e1', label='p1', linewidth=1)
    plt.plot(y3, color='#99cc00', label='p2', linewidth=1)

    plt.legend(['True', 'P2'])  # 设置折线名称
    # plt.legend(['True', 'P1', 'P2'])  # 设置折线名称
    plt.show()  # 显示折线图







if __name__ == '__main__':
    print("Welcome to MyTools!")
    l1 = txtReadNumArray("./example/data/true.txt")
    l2 = txtReadNumArray("./example/data/p1.txt")
    l3 = txtReadNumArray("./example/data/p2.txt")
    plot_line_chart(l1[120:8000],l2[0:8000],l3[0:8000])

