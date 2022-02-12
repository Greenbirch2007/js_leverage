# -*- coding:utf-8 -*-
import datetime
import re
import time
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import pymysql

from lxml import etree
from selenium import webdriver
from bs4 import BeautifulSoup

import requests



def get_first_page(url):
    ch_options = webdriver.ChromeOptions()
    # 为Chrome配置无头模式
    # ch_options.add_argument("--headless")
    # ch_options.add_argument('--no-sandbox')
    # ch_options.add_argument('--disable-gpu')
    # ch_options.add_argument('--disable-dev-shm-usage')
    # 在启动浏览器时加入配置
    # driver = webdriver.Chrome(options=ch_options)
    respnse = requests.get(url)
    html = respnse.text
    return html

# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find_all("th"))


    time.sleep(6)

# //*[@id="stock_holder"]/table[1]/tbody/tr/th/text()
# //*[@id="stock_holder"]/table[1]/tbody/tr/th/*/text()

# //th/text()




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into nihonNEWS_js_FinData (d2017,d2018,d2019, d2020,d2021,industry,coding,title,market_value,returns_ratio,min_callshares) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

#
if __name__ == '__main__':
    # graphviz = GraphvizOutput()
    # graphviz.output_file = 'basic.png'
    # with PyCallGraph(output=graphviz):

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    options = webdriver.ChromeOptions()


    #sql 语句
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

    for num_coding in js225_400_codes:
        big_list = []
        url = 'https://kabutan.jp/stock/holder?code={0}'.format(num_coding)
        print(url)

        html = get_first_page(url)
        # time.sleep(3)
        content = parse_stock_note(html)
        print(content)
        # for item in content:
        #     big_list.append(item)
        # # 加入查询板块的操作
        # sql = 'select * from js_infos_finanData where coding = %s ' % num_coding
        # # #执行sql语句
        # cur.execute(sql)
        # # #获取所有记录列表
        # data = cur.fetchone()
        # try:
        #
        #     data_industry = data['industry']
        #     big_list.append(data_industry)
        #     data_coding = data['coding']
        #     big_list.append(data_coding)
        #     data_title = data['title']
        #     big_list.append(data_title)
        #     data_market_value = data['market_value']
        #     big_list.append(data_market_value)
        #     data_returns_ratio = data['returns_ratio']
        #     big_list.append(data_returns_ratio)
        #     data_min_callshares = data['min_callshares']
        #     big_list.append(data_min_callshares)
        #     big_list_tuple = tuple(big_list)
        #     finanl_content = []
        #     finanl_content.append(big_list_tuple)  # 是要带着元括号操作，
        #     print(big_list_tuple)
        #     insertDB(finanl_content)
        #     print(datetime.datetime.now())
        # except:
        #     pass

# <th scope="row" class="">(.*?)</th>

# 因为板块数据是最后嵌套进去的，所以要保持，１．数据库表结构，２．解析整理后的数据结构　３．　插入的字段结构　三者之间都要保持一致
# create table nihonNEWS_js_FinData(
# id int not null primary key auto_increment,
# d2017 varchar(20),
# d2018 varchar(20),
# d2019 varchar(20),
# d2020 varchar(20),
# d2021 varchar(20),
# industry varchar(8),
# coding varchar(11),
# title varchar(60),
# market_value varchar(20),
# returns_ratio varchar(6),
# min_callshares varchar(11)
# ) engine=InnoDB  charset=utf8;

#  drop table nihonNEWS_js_FinData;


#


