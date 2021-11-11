'''
img tools
包含图片处理常见工具.
function:
1. 根据路径返回img
'''

import cv2

def get_img(getpath):
    img = cv2.imread(getpath)
    return img

def save_img(savepath, img):
    cv2.imwrite(savepath, img)












if __name__ == '__main__':
    print("Welcome to MyTools!")
