import numpy as np
from skimage import draw, data

'''
生成方形中间为圆，圆value=y 边value=x 的box
(方长, 圆形位置, 半径, 方值, 圆值)
'''
def box_circle(box_length, center, radius, x, y): 
    box = np.full((box_length, box_length), x)
    rr, cc=draw.disk(center,radius)
    box[rr, cc] = y
    # print(box.sum())
    return box
