import datetime
import time
from lxml import etree

import requests
import re
import pymysql
#特殊异常要先引入
from requests.exceptions import RequestException
#请求页面 #反爬虫升级 ，js渲染，selenium
from selenium import webdriver


def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None





def parse_stock_note(html):
    selector = etree.HTML(html)
    coding_ = selector.xpath('//*[@id="industry"]/span/text()')
    industry_ = selector.xpath('//*[@id="industry"]/a/text()')
    title_= selector.xpath('//*[@id="root"]/main/div/div/div[1]/div[2]/section[1]/div[2]/header/div[1]/h1/text()')
    last_price_ = selector.xpath('//*[@id="root"]/main/div/div/div[1]/div[2]/section[1]/div[2]/header/div[2]/span/span/span/text()')
    market_value_= selector.xpath('//*[@id="referenc"]/div/ul/li[1]/dl/dd/span[1]/span/span[1]/text()')
    share_nums_= selector.xpath('//*[@id="referenc"]/div/ul/li[2]/dl/dd/span[1]/span/span[1]/text()')
    returns_ratio_= selector.xpath('//*[@id="referenc"]/div/ul/li[3]/dl/dd/span[1]/span/span[1]/text()')
    min_callshares_= selector.xpath('//*[@id="referenc"]/div/ul/li[9]/dl/dd/span[1]/span/span/text()')
    big_tuple = [(coding_[0],industry_[0],title_[0],last_price_[0],market_value_[0],share_nums_[0],returns_ratio_[0],min_callshares_[0])]
    return big_tuple



# 查询的方法
def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标

    js225_400_codes = ['1332', '1333', '1417', '1605', '1719', '1720', '1721', '1766', '1801', '1802', '1803', '1808',
                       '1812', '1820', '1821', '1824', '1860', '1861', '1878', '1881', '1893', '1911', '1925', '1928',
                       '1942', '1951', '1959', '1963', '1973', '2002', '2121', '2127', '2146', '2175', '2181', '2201',
                       '2229', '2264', '2267', '2269', '2281', '2282', '2317', '2327', '2331', '2337', '2371', '2379',
                       '2412', '2413', '2427', '2432', '2433', '2501', '2502', '2503', '2531', '2587', '2593', '2651',
                       '2670', '2702', '2768', '2782', '2784', '2801', '2802', '2809', '2811', '2815', '2871', '2875',
                       '2897', '2914', '3003', '3038', '3048', '3064', '3086', '3088', '3092', '3099', '3101', '3103',
                       '3107', '3116', '3141', '3148', '3167', '3231', '3244', '3254', '3288', '3289', '3291', '3349',
                       '3360', '3382', '3391', '3401', '3402', '3405', '3407', '3436', '3543', '3549', '3563', '3626',
                       '3635', '3659', '3738', '3765', '3769', '3861', '3863', '3880', '3923', '3932', '3941', '4004',
                       '4005', '4021', '4042', '4043', '4061', '4063', '4088', '4091', '4151', '4182', '4183', '4188',
                       '4202', '4204', '4205', '4206', '4208', '4307', '4324', '4348', '4403', '4452', '4502', '4503',
                       '4506', '4507', '4516', '4519', '4521', '4523', '4527', '4528', '4536', '4543', '4552', '4553',
                       '4568', '4578', '4587', '4612', '4613', '4631', '4661', '4684', '4686', '4689', '4704', '4716',
                       '4732', '4739', '4751', '4755', '4768', '4812', '4816', '4819', '4848', '4849', '4887', '4901',
                       '4902', '4911', '4912', '4921', '4922', '4927', '4967', '5019', '5020', '5021', '5101', '5105',
                       '5108', '5110', '5201', '5202', '5214', '5232', '5233', '5301', '5332', '5333', '5334', '5393',
                       '5401', '5406', '5411', '5541', '5631', '5703', '5706', '5707', '5711', '5713', '5714', '5801',
                       '5802', '5803', '5857', '5929', '5947', '6005', '6028', '6035', '6055', '6098', '6103', '6113',
                       '6134', '6136', '6141', '6146', '6178', '6183', '6201', '6235', '6268', '6273', '6301', '6302',
                       '6305', '6326', '6361', '6367', '6383', '6432', '6448', '6465', '6471', '6472', '6473', '6479',
                       '6501', '6503', '6504', '6506', '6532', '6544', '6586', '6594', '6645', '6670', '6674', '6701',
                       '6702', '6703', '6723', '6724', '6727', '6728', '6750', '6752', '6753', '6754', '6758', '6762',
                       '6770', '6841', '6845', '6849', '6856', '6857', '6861', '6869', '6902', '6920', '6923', '6952',
                       '6954', '6965', '6971', '6976', '6981', '6988', '7003', '7004', '7011', '7012', '7013', '7148',
                       '7164', '7167', '7177', '7186', '7201', '7202', '7203', '7205', '7211', '7259', '7261', '7267',
                       '7269', '7270', '7272', '7276', '7282', '7309', '7313', '7419', '7453', '7459', '7516', '7532',
                       '7550', '7564', '7575', '7649', '7701', '7717', '7729', '7731', '7733', '7735', '7741', '7747',
                       '7751', '7752', '7762', '7832', '7846', '7911', '7912', '7947', '7951', '7956', '7974', '7988',
                       '8001', '8002', '8015', '8020', '8031', '8035', '8053', '8056', '8058', '8088', '8111', '8113',
                       '8194', '8233', '8252', '8253', '8267', '8273', '8279', '8282', '8283', '8303', '8304', '8306',
                       '8308', '8309', '8316', '8331', '8354', '8355', '8410', '8411', '8424', '8425', '8439', '8473',
                       '8570', '8572', '8585', '8591', '8593', '8595', '8601', '8604', '8628', '8630', '8697', '8725',
                       '8750', '8766', '8795', '8801', '8802', '8804', '8830', '8850', '8876', '8892', '8905', '8919',
                       '9001', '9005', '9007', '9008', '9009', '9020', '9021', '9022', '9042', '9062', '9064', '9065',
                       '9069', '9086', '9090', '9101', '9104', '9107', '9142', '9143', '9202', '9301', '9375', '9418',
                       '9432', '9433', '9434', '9435', '9501', '9502', '9503', '9504', '9506', '9508', '9509', '9513',
                       '9517', '9519', '9531', '9532', '9602', '9613', '9627', '9678', '9684', '9697', '9719', '9735',
                       '9744', '9766', '9787', '9810', '9843', '9962', '9983', '9984', '9989']

    for i in js225_400_codes:
        url = "https://finance.yahoo.co.jp/quote/{0}.T".format(i)
        yield url





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into js_infos_finanData (coding,industry,title,last_price,market_value,share_nums,returns_ratio,min_callshares) values (%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':

    for url_str in Python_sel_Mysql():
        html = call_page(url_str)
        content = parse_stock_note(html)
        insertDB(content)
        print(content)






# # name是mysql的关键字！
# create table js_infos_finanData(
# id int not null primary key auto_increment,
# coding varchar(11),
# industry varchar(8),
# title varchar(60),
# last_price varchar(20),
# market_value varchar(20),
# share_nums varchar(30),
# returns_ratio varchar(6),
# min_callshares varchar(11)
# ) engine=InnoDB default charset=utf8;




# drop table js_infos_finanData;

