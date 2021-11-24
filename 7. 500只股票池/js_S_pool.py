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
    pool_data =["1820","1821","2267","2331","2427","2503","3092","3436","3626","3765","3769","4021","4403","4507","4543","4684","4716","4751","4755","4768","4921","5214","5631","5713","5802","6134","6235","6273","6326","6361","6471","6504","6506","6674","6727","6728","6753","6762","6845","6869","6902","6976","7211","7259","7701","7741","7762","7947","8002","8031","8035","8058","8113","8303","8304","8473","8919","9086","9434","9506","9519","9613","9627"]


    for coding in pool_data:
        call_url(coding)
        print(coding)
    print("图片下载完毕")
