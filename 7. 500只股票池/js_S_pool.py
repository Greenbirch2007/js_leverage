# 1.股票池的相关数据
# 2.股票池子的走势图整理！
# 3.用execl函数提取代码　　=MID(B2,LEN(B2)-4,4)
import re
import time
import urllib.request

from retrying import retry
from urllib.error import URLError
import os


def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求
@retry(retry_on_exception=retry_if_io_error)
def call_url(coding):
    l_path = os.getcwd()
    url = 'https://chart.yahoo.co.jp/?code=' + str(coding) + '.T&tm=1y&type=c&log=off&size=m&over=m65,m130,s&add=v&comp='
    urllib.request.urlretrieve(url, '{0}/{1}.jpg'.format(l_path,coding))




if __name__=='__main__':

# 2020.8.25
    pool_data =["5707","9517","7747","5021","9101","5541","9104","1605","4527","9107","5714","5019","3064","7846","7011","2317","7532","3659","5713","4922","2267","4704","3088","2201","6856","1812","4612","3349","3769","7832","1719","3038","9086","8088","8002","4568","7912","2802","9532","6361","9432","1911","8053","5706","5401","9502","9503","7564","2768","4848","9509","9843","7013","5857","5406","1721","9501","9434","1820","9508","5411","8595","1963","8919","1417","5020","3391","2811","2897","5703","7575","2432","9064","4967","2809","9433","8020","7974","2587","6841","2784","9989","7202","1942","9504","1951","9301","6273","4819","8001","5711","9810","4182","1801","9531","9375","8892","6750"]




    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
