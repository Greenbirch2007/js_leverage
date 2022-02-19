
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine

import pandas as pd

month_dbname =["js225_400_leverage_2021_1024","js225_400_leverage_2021_1116",
               "js225_400_leverage_2021_1228","js225_400_leverage_2022_0122"]



def savedt():
    for one_month in month_dbname:
        engine_jsMons = create_engine('mysql+pymysql://root:123456@localhost:3306/JS')
        sql_sp_LJ = 'select  id from {0}  ; '.format(one_month)
        df_js = pd.read_sql_query(sql_sp_LJ.format("J225"), engine_jsMons)
        max_id = len(df_js)
        sql_sp_f = 'select * from {1}  where id ={0} ; '
        df_js_f = pd.read_sql_query(sql_sp_f.format(max_id,month_dbname), engine_jsMons)
        df_js_f.to_excel("{0}.xlsx".format(one_month))



if __name__ == '__main__':
    savedt()


