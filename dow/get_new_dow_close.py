import yahoo_fin.stock_info as si
import yahoo_fin.options as ops
import pandas as pd
from datetime import date

today = date.today()
d1 = today.strftime("%m/%d/%y")

# get list of dow tickers
dow_list = si.tickers_dow()
#f = open("dict_dow.json", "w")
# pull data for each dow stock
dow_price_data = {}
for ticker in dow_list:
    temp = si.get_data(ticker, start_date = d1)
    temp = temp.iloc[:,4:5]
    temp.columns = ["close"]
    dow_price_data[ticker] = temp

combined_stats = pd.concat(dow_price_data)
combined_stats = combined_stats.reset_index()
# del combined_stats["level_0"]
# update column names
combined_stats.columns = ["Ticker", "Date", "Close"]
combined_stats.to_csv (r'/home/jordysjoint/export_new_dow.csv', index = False, header = True)
#f.write(dow_price_data)
#f.close()

