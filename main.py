import json
from typing import List
from db import local_db
from patterns import *
import pandas as pd
import datetime
from api_yahoo import get_info_data
from fastapi import FastAPI
from pydantic import BaseModel


class basic_info(BaseModel):
    stock_name : str
    up_trends : bool
    start_d  = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    end_d = datetime.date.today().strftime('%Y-%m-%d')
    interval_t = "1d"
    price_trigger : float


class stocks(BaseModel):
    stock_name: List[basic_info]


stocks_list = stocks(stock_name=local_db())

app = FastAPI()

@app.post("/db-alerts-stocks")
async def get_alert():
    dic = {}
    for stock in stocks_list.stock_name:

        cur_price =  get_info_data(stock.stock_name, stock.start_d, stock.end_d, stock.interval_t)

        if stock.up_trends:
            result = up_trend(cur_price, stock.price_trigger, stock.stock_name)
            if result: 
                dic.update({stock.stock_name : f' in trigger and cut up {stock.price_trigger}$'})
            else:
                dic.update({stock.stock_name:' is not in trigger'})
        else:
            result = down_trend(cur_price, stock.price_trigger, stock.stock_name)

            if result: 
                dic.update({stock.stock_name : f' in trigger and cut down {stock.price_trigger}$'})
            else:
                dic.update({stock.stock_name:' is not in trigger'})

    return json.dumps(dic,ensure_ascii=False)