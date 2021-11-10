'''
获取当前时间方便文件命名
'''
import datetime


now = datetime.datetime.now()

# 返回 年月日 时分秒 毫秒
def getDateYMDHMSU():
    return now.strftime('%Y%m%d_%H%M%S_%U')

# 返回年月日
def getDateYMD():
    return now.strftime('%Y%m%d')

# 返回 年月日 时分秒
def getDateYMDHMSU():
    return now.strftime('%Y%m%d_%H%M%S')

if __name__=='__main__':
    print(getDateYMDHMSU())
    print(getDateYMD())
