#
#
# js   js_infos_finandata
# coding industry title market
import csv
import time

import pandas as pd
import pymysql

df = pd.read_excel("demo.xlsx")
df_list = list(df)
# ['Unnamed: 0', 'J225', 'J400', 'J1605', 'J1820', 'J1821', 'J1928', 'J2267', 'J2282', 'J2433', 'J2702', 'J2768', 'J2801', 'J2875', 'J2914', 'J3038', 'J3254', 'J3291', 'J3626', 'J3941', 'J4061', 'J4204', 'J4307', 'J4507', 'J4527', 'J4528', 'J4543', 'J4684', 'J4732', 'J4768', 'J4902', 'J5108', 'J5214', 'J5232', 'J5334', 'J5393', 'J5631', 'J6055', 'J6146', 'J6178', 'J6235', 'J6273', 'J6326', 'J6361', 'J6367', 'J6448', 'J6472', 'J6479', 'J6504', 'J6506', 'J6594', 'J6645', 'J6674', 'J6724', 'J6727', 'J6728', 'J6758', 'J6845', 'J6857', 'J6861', 'J6869', 'J6902', 'J6920', 'J6954', 'J6965', 'J6971', 'J6976', 'J6981', 'J6988', 'J7148', 'J7259', 'J7459', 'J7550', 'J7701', 'J7731', 'J7733', 'J7735', 'J7751', 'J7846', 'J7911', 'J7912', 'J7974', 'J8001', 'J8002', 'J8031', 'J8035', 'J8053', 'J8058', 'J8113', 'J8303', 'J8309', 'J8424', 'J8473', 'J8593', 'J8697', 'J8766', 'J8804', 'J8919', 'J9062', 'J9064', 'J9086', 'J9101', 'J9104', 'J9107', 'J9375', 'J9502', 'J9503', 'J9504', 'J9506', 'J9508', 'J9509', 'J9513', 'J9531', 'J9532', 'J9719', 'J9735', 'J9810', 'LastTime']
index_title =df_list[3:-1]
# #not 225  400


def writeinto_detail(filename,data):
    with open(filename,"a",newline="",encoding="utf-8-sig") as f:
        csv_out = csv.writer(f,delimiter=",")
        csv_out.writerow(data)
writeinto_detail("followed_detail.csv",["serverid","vaule","title","industry","coding","min_callshares","market_value","returns_ratio"])
for one_stock in index_title:
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    sql = "select coding,industry,title,market_value,returns_ratio,min_callshares from js_infos_finanData where coding={0}; ".format(one_stock[1:])
    cur.execute(sql)
    # #获取所有记录列表
    data = cur.fetchone()
    print(data)
    title = data["title"]
    coding = data["coding"]
    industry = data["industry"]
    min_callshares = data["min_callshares"]
    market_value = data["market_value"]
    returns_ratio = data["returns_ratio"]
    detail_data = [one_stock,list(df[one_stock])[-1],title,industry,coding,min_callshares,market_value,returns_ratio]
    print(detail_data)
    writeinto_detail("followed_detail.csv",detail_data)
    cur.close()

writeinto_detail("followed_detail.csv", ["J225",list(df["J225"])[-1]])
writeinto_detail("followed_detail.csv", ["J400",list(df["J400"])[-1]])









