import os

import pymysql
import csv

# 数据处理好，看如何塞入execl中


def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True



if __name__ =='__main__':
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    # sql 语句
    count_sql = "select count(*) from nihonNEWS_js_FinData; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count):


        sql = 'select d2021, d2020, d2019, d2018, d2017, industry,coding,title,market_value,returns_ratio,min_callshares from nihonNEWS_js_FinData where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)
    print(big_list)
    l_path = os.getcwd()
    head = ['d2021',"d2020","d2019","d2018","d2017","industry","coding","title","market_value","returns_ratio","min_callshares"]
    csv_dict_write('{0}\\nihonNEWS_js_FinData.csv'.format(l_path),head,big_list)
    print("数据导出完成～")

