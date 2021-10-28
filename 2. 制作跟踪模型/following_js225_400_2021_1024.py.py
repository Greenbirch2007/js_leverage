


import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry

def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)







def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


class JSPool_M(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="layout"]/div[2]/div[3]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(float(f_price[0]))
        print(f_price[0])
        return big_list



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    try:
        # 用一个列表解析
        f_jsp = ["J" + cod for cod in into_db]
        sp_func = lambda x: ",".join(x)
        f_lcode = sp_func(f_jsp)

        f_ls = "%s," * len(into_db)
        fc = f_lcode
        print(len(fc.split(",")))
        print(len(f_ls[:-1].split(",")))
        cursor.executemany('insert into js225_400_leverage_2021_1024 ({0}) values ({1})'.format(fc,f_ls[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass




def get_index():
    index_code = ["0000", "0040"]
    for i_code in index_code:
        url ='https://kabutan.jp/stock/?code={0}'.format(i_code)
        html =call_page(url)
        element = etree.HTML(html)

        now_price = element.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(float(f_price[0]))




if __name__ == "__main__":
    s = datetime.datetime.now()
    into_db =  ["225","400",'1332','1333', '1417', '1605', '1719', '1720', '1721', '1766', '1801', '1802', '1803', '1808',
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
    big_list = []
    f_compare_content = []
    get_index()
    _2021_10_23=[28804.85, 18043.77, 645.0, 2593.0, 2192.0, 951.0, 769.0, 809.0, 2873.0, 9430.0, 3635.0, 969.0, 857.0, 1486.0, 1436.0, 3400.0, 492.0, 899.0, 735.0, 2801.0, 13620.0, 4035.0, 774.0, 2099.0, 3722.0, 2322.0, 898.0, 2647.0, 3555.0, 1108.0, 2051.0, 1791.0, 2661.0, 3505.0, 3510.0, 4355.0, 2897.0, 3975.0, 2729.0, 6670.0, 5740.0, 7030.0, 2710.0, 4010.0, 2126.0, 3740.0, 4970.0, 334.0, 3650.0, 4105.0, 5490.0, 7397.0, 2018.0, 2154.0, 1857.0, 2498.0, 5084.0, 2005.0, 1567.0, 4415.0, 7140.0, 5330.0, 5620.0, 5080.0, 1895.0, 3805.0, 1638.0, 9100.0, 3349.0, 2484.0, 2844.0, 7220.0, 2781.0, 4735.0, 8730.0, 2251.0, 1107.0, 3850.0, 989.0, 2581.0, 1054.0, 5020.0, 4200.0, 822.0, 1363.0, 361.0, 1937.0, 2089.0, 4150.0, 3580.0, 888.0, 2860.0, 2390.0, 1862.0, 6900.0, 663.0, 2816.0, 17550.0, 2883.0, 4745.0, 13800.0, 1560.0, 708.0, 1048.0, 1215.0, 2149.0, 2062.0, 7510.0, 4935.0, 3080.0, 5170.0, 1993.0, 2049.0, 2128.0, 14400.0, 562.0, 1173.0, 1972.0, 3380.0, 3190.0, 864.0, 2880.0, 578.0, 6330.0, 1923.0, 2009.0, 3795.0, 19125.0, 1714.0, 2633.0, 3690.0, 2355.0, 3480.0, 965.0, 860.0, 1779.0, 1464.0, 3570.0, 2185.0, 4205.0, 4120.0, 2379.0, 5620.0, 6391.0, 3203.0, 1957.0, 1896.0, 7527.0, 8940.0, 3841.0, 4480.0, 8039.0, 3385.0, 2459.0, 1586.0, 5050.0, 2849.0, 3540.0, 2750.0, 4648.0, 2549.0, 1260.0, 2608.0, 3035.0, 18000.0, 21620.0, 5850.0, 663.0, 6340.0, 10420.0, 1789.0, 3615.0, 1985.0, 1244.0, 5740.0, 3970.0, 20260.0, 4970.0, 2581.0, 4670.0, 5030.0, 8853.0, 589.0, 7363.0, 1905.0, 3465.0, 14110.0, 2490.0, 8620.0, 3240.0, 465.0, 2454.0, 1969.0, 1858.0, 5101.0, 1433.0, 5700.0, 636.0, 2825.0, 3300.0, 2440.0, 1461.0, 5730.0, 1904.0, 1710.0, 2716.0, 1940.0, 649.0, 1678.0, 2060.0, 3335.0, 1922.0, 3320.0, 3195.0, 2218.0, 4382.0, 4790.0, 2559.0, 1526.0, 661.0, 2195.0, 1416.0, 11670.0, 4305.0, 3615.0, 10480.0, 1521.0, 7015.0, 5400.0, 1138.0, 2590.0, 1844.0, 1927.0, 31000.0, 876.0, 1561.0, 9560.0, 2274.0, 3930.0, 67740.0, 2892.0, 2826.0, 3405.0, 2397.0, 6130.0, 25580.0, 10320.0, 2900.0, 2320.0, 9740.0, 802.0, 265.0, 1027.0, 2815.0, 6685.0, 1583.0, 5040.0, 4955.0, 45650.0, 2383.0, 5660.0, 12590.0, 10620.0, 1251.0, 2525.0, 6250.0, 21490.0, 956.0, 1391.0, 2124.0, 723.0, 6250.0, 1710.0, 1378.0, 1372.0, 2092.0, 12815.0, 3915.0, 1162.0, 2203.0, 4805.0, 3660.0, 7560.0, 9110.0, 67210.0, 13995.0, 7793.0, 25810.0, 2825.0, 1663.0, 24395.0, 6690.0, 6702.0, 5530.0, 8476.0, 8020.0, 553.0, 868.0, 2982.0, 2358.0, 2697.0, 697.0, 5360.0, 238.0, 882.0, 467.0, 587.0, 1497.0, 1983.0, 1114.0, 369.0, 4165.0, 1048.0, 3417.0, 5110.0, 2275.0, 3140.0, 6610.0, 2305.0, 29680.0, 1508.0, 2810.0, 2214.0, 2133.0, 3610.0, 2431.0, 2621.0, 6140.0, 1285.0, 8160.0, 4625.0, 4335.0, 4505.0, 1298.0, 2508.0, 9480.0, 17360.0, 3000.0, 2847.0, 1129.0, 512.0, 8670.0, 4240.0, 1852.0, 2818.0, 3865.0, 7120.0, 2481.0, 50020.0, 3600.0, 3250.0, 949.0, 4885.0, 1333.0, 2574.0, 50750.0, 1599.0, 3145.0, 3559.0, 6700.0, 6560.0, 4410.0, 3735.0, 1107.0, 2245.0, 1441.0, 2617.0, 3655.0, 6670.0, 1191.0, 5220.0, 1910.0, 2693.0, 652.0, 440.0, 3860.0, 3865.0, 733.0, 2114.0, 947.0, 246.0, 1530.0, 7490.0, 3525.0, 6650.0, 2989.0, 1482.0, 388.0, 158.0, 2148.0, 575.0, 7900.0, 665.0, 554.0, 822.0, 4918.0, 2762.0, 3688.0, 2425.0, 6103.0, 1518.0, 2611.0, 1754.0, 1674.0, 4098.0, 2780.0, 2354.0, 810.0, 1718.0, 4060.0, 2854.0, 1621.0, 2494.0, 5820.0, 3685.0, 7270.0, 5323.0, 17045.0, 3485.0, 7420.0, 2814.0, 5220.0, 1030.0, 4860.0, 1548.0, 7770.0, 6560.0, 5060.0, 2578.0, 2850.0, 2699.0, 3215.0, 2742.0, 3255.0, 3120.0, 3689.0, 1530.0, 17870.0, 339.0, 1291.0, 1072.0, 988.0, 774.0, 836.0, 519.0, 1551.0, 2597.0, 4760.0, 1894.0, 1888.0, 5470.0, 2214.0, 6700.0, 2478.0, 6150.0, 3375.0, 2320.0, 7863.0, 6600.0, 6540.0, 3370.0, 4975.0, 19965.0, 4795.0, 72780.0, 6610.0, 3445.0]

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



    for it in js225_400_codes:

        url = "https://minkabu.jp/stock/{0}".format(it)
        print(url)
        jsp = JSPool_M(url)# 这里把请求和解析都进行了处理
        jsp.page_parse_()
    ff_l = []
    print(len(_2021_10_23[2:]))
    print(len(big_list[2:]))
    index225_ = (big_list[0] - _2021_10_23[0]) / _2021_10_23[0]
    index400_ = (big_list[1] - _2021_10_23[1]) / _2021_10_23[1]

    f_compare_content.append(str(round(index225_,5)))
    f_compare_content.append(str(round(index400_,5)))

    for i1,i2 in zip(big_list[2:],_2021_10_23[2:]):
        if (((i1-i2)/i2)-0.03) > max(float(f_compare_content[0]),float(f_compare_content[1])):
            print((i1-float(i2))/float(i2)-0.05)
            print(max(index225_,index400_))

            f_compare_content.append(round(((i1-i2)/i2),5))
        else:
            print(round(((i1-float(i2))/float(i2))))
            f_compare_content.append("null")


    f_tup = tuple(f_compare_content)
    print(f_tup)
    ff_l.append((f_tup))
    print(ff_l)
    print(big_list)
    print(f_compare_content)
    insertDB(ff_l)
    e = datetime.datetime.now()
    print(e-s)





















 #   create table js225_400_leverage_2021_1024(id int not null primary key auto_increment,J225 float,J400 float,J1332 float, J1333 float, J1417 float, J1605 float, J1719 float, J1720 float, J1721 float, J1766 float, J1801 float, J1802 float, J1803 float, J1808 float, J1812 float, J1820 float, J1821 float, J1824 float, J1860 float, J1861 float, J1878 float, J1881 float, J1893 float, J1911 float, J1925 float, J1928 float, J1942 float, J1951 float, J1959 float, J1963 float, J1973 float, J2002 float, J2121 float, J2127 float, J2146 float, J2175 float, J2181 float, J2201 float, J2229 float, J2264 float, J2267 float, J2269 float, J2281 float, J2282 float, J2317 float, J2327 float, J2331 float, J2337 float, J2371 float, J2379 float, J2412 float, J2413 float, J2427 float, J2432 float, J2433 float, J2501 float, J2502 float, J2503 float, J2531 float, J2587 float, J2593 float, J2651 float, J2670 float, J2702 float, J2768 float, J2782 float, J2784 float, J2801 float, J2802 float, J2809 float, J2811 float, J2815 float, J2871 float, J2875 float, J2897 float, J2914 float, J3003 float, J3038 float, J3048 float, J3064 float, J3086 float, J3088 float, J3092 float, J3099 float, J3101 float, J3103 float, J3107 float, J3116 float, J3141 float, J3148 float, J3167 float, J3231 float, J3244 float, J3254 float, J3288 float, J3289 float, J3291 float, J3349 float, J3360 float, J3382 float, J3391 float, J3401 float, J3402 float, J3405 float, J3407 float, J3436 float, J3543 float, J3549 float, J3563 float, J3626 float, J3635 float, J3659 float, J3738 float, J3765 float, J3769 float, J3861 float, J3863 float, J3880 float, J3923 float, J3932 float, J3941 float, J4004 float, J4005 float, J4021 float, J4042 float, J4043 float, J4061 float, J4063 float, J4088 float, J4091 float, J4151 float, J4182 float, J4183 float, J4188 float, J4202 float, J4204 float, J4205 float, J4206 float, J4208 float, J4307 float, J4324 float, J4348 float, J4403 float, J4452 float, J4502 float, J4503 float, J4506 float, J4507 float, J4516 float, J4519 float, J4521 float, J4523 float, J4527 float, J4528 float, J4536 float, J4543 float, J4552 float, J4553 float, J4568 float, J4578 float, J4587 float, J4612 float, J4613 float, J4631 float, J4661 float, J4684 float, J4686 float, J4689 float, J4704 float, J4716 float, J4732 float, J4739 float, J4751 float, J4755 float, J4768 float, J4812 float, J4816 float, J4819 float, J4848 float, J4849 float, J4887 float, J4901 float, J4902 float, J4911 float, J4912 float, J4921 float, J4922 float, J4927 float, J4967 float, J5019 float, J5020 float, J5021 float, J5101 float, J5105 float, J5108 float, J5110 float, J5201 float, J5202 float, J5214 float, J5232 float, J5233 float, J5301 float, J5332 float, J5333 float, J5334 float, J5393 float, J5401 float, J5406 float, J5411 float, J5541 float, J5631 float, J5703 float, J5706 float, J5707 float, J5711 float, J5713 float, J5714 float, J5801 float, J5802 float, J5803 float, J5857 float, J5929 float, J5947 float, J6005 float, J6028 float, J6035 float, J6055 float, J6098 float, J6103 float, J6113 float, J6134 float, J6136 float, J6141 float, J6146 float, J6178 float, J6183 float, J6201 float, J6235 float, J6268 float, J6273 float, J6301 float, J6302 float, J6305 float, J6326 float, J6361 float, J6367 float, J6383 float, J6432 float, J6448 float, J6465 float, J6471 float, J6472 float, J6473 float, J6479 float, J6501 float, J6503 float, J6504 float, J6506 float, J6532 float, J6544 float, J6586 float, J6594 float, J6645 float, J6670 float, J6674 float, J6701 float, J6702 float, J6703 float, J6723 float, J6724 float, J6727 float, J6728 float, J6750 float, J6752 float, J6753 float, J6754 float, J6758 float, J6762 float, J6770 float, J6841 float, J6845 float, J6849 float, J6856 float, J6857 float, J6861 float, J6869 float, J6902 float, J6920 float, J6923 float, J6952 float, J6954 float, J6965 float, J6971 float, J6976 float, J6981 float, J6988 float, J7003 float, J7004 float, J7011 float, J7012 float, J7013 float, J7148 float, J7164 float, J7167 float, J7177 float, J7186 float, J7201 float, J7202 float, J7203 float, J7205 float, J7211 float, J7259 float, J7261 float, J7267 float, J7269 float, J7270 float, J7272 float, J7276 float, J7282 float, J7309 float, J7313 float, J7419 float, J7453 float, J7459 float, J7516 float, J7532 float, J7550 float, J7564 float, J7575 float, J7649 float, J7701 float, J7717 float, J7729 float, J7731 float, J7733 float, J7735 float, J7741 float, J7747 float, J7751 float, J7752 float, J7762 float, J7832 float, J7846 float, J7911 float, J7912 float, J7947 float, J7951 float, J7956 float, J7974 float, J7988 float, J8001 float, J8002 float, J8015 float, J8020 float, J8031 float, J8035 float, J8053 float, J8056 float, J8058 float, J8088 float, J8111 float, J8113 float, J8194 float, J8233 float, J8252 float, J8253 float, J8267 float, J8273 float, J8279 float, J8282 float, J8283 float, J8303 float, J8304 float, J8306 float, J8308 float, J8309 float, J8316 float, J8331 float, J8354 float, J8355 float, J8410 float, J8411 float, J8424 float, J8425 float, J8439 float, J8473 float, J8570 float, J8572 float, J8585 float, J8591 float, J8593 float, J8595 float, J8601 float, J8604 float, J8628 float, J8630 float, J8697 float, J8725 float, J8750 float, J8766 float, J8795 float, J8801 float, J8802 float, J8804 float, J8830 float, J8850 float, J8876 float, J8892 float, J8905 float, J8919 float, J9001 float, J9005 float, J9007 float, J9008 float, J9009 float, J9020 float, J9021 float, J9022 float, J9042 float, J9062 float, J9064 float, J9065 float, J9069 float, J9086 float, J9090 float, J9101 float, J9104 float, J9107 float, J9142 float, J9143 float, J9202 float, J9301 float, J9375 float, J9418 float, J9432 float, J9433 float, J9434 float, J9435 float, J9501 float, J9502 float, J9503 float, J9504 float, J9506 float, J9508 float, J9509 float, J9513 float, J9517 float, J9519 float, J9531 float, J9532 float, J9602 float, J9613 float, J9627 float, J9678 float, J9684 float, J9697 float, J9719 float, J9735 float, J9744 float, J9766 float, J9787 float, J9810 float, J9843 float, J9962 float, J9983 float, J9984 float, J9989 float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;



