import yahoo_fin.stock_info as si
import yahoo_fin.options as ops
import pandas as pd
from datetime import date

today = date.today()
d1 = today.strftime("%m/%d/%y")

# get list of dow tickers
dow_list = si.tickers_dow()

# pull data for each dow stock and pass any expections
dow_price_data = {}
for ticker in dow_list:
    try:
        temp = si.get_data(ticker, start_date = "01/01/2010", end_date = d1)
        temp = temp.iloc[:,4:5]
        temp.columns = ["close"]
        dow_price_data[ticker] = temp
    except Exception:
        pass

# clean up the table and add column header names
combined_stats = pd.concat(dow_price_data)
combined_stats = combined_stats.reset_index()
combined_stats.columns = ["Ticker", "Date", "Close"]

# convert the dataframe to a csv file
combined_stats.to_csv (r'/home/jordysjoint/export_dow.csv', index = False, header = True)


