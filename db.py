from doctest import FAIL_FAST


def local_db():    ### Local db
    db_stocks = [{"stock_name":"TSLA", "up_trends":True,  "price_trigger":50},
               {"stock_name":"AAPL",   "up_trends":True,  "price_trigger":150},
               {"stock_name":"NVDA",   "up_trends":False, "price_trigger":150},
               {"stock_name":"FB",     "up_trends":False, "price_trigger":250}]

    return db_stocks