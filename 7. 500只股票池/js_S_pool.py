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
    pool_data =["2146","3288","4506","4519","4587","5202","5301","5401","5406","5411","5541","5707","6035","6098","6302","6752","6758","6762","6841","7004","7988","8591","9104","9107","9432","9684",
]
    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
