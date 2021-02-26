import yahoo_fin.stock_info as si
import yahoo_fin.options as ops
import pandas as pd
from datetime import date

#get today's date
today = date.today()
d1 = today.strftime("%m/%d/%y")

# get list of s&p500 tickers
sp_list = si.tickers_sp500()

# pull data for each s&p500 stock and pass any exceptions
sp_price_data = {}
for ticker in sp_list:
    try:
        temp = si.get_data(ticker, start_date = d1)
        temp = temp.iloc[:,4:5]
        temp.columns = ["close"]
        sp_price_data[ticker] = temp
    except Exception:
        pass

# clean up the table and update the column names
combined_stats = pd.concat(sp_price_data)
combined_stats = combined_stats.reset_index()
combined_stats.columns = ["Ticker", "Date", "Close"]

# convert the dataframe into a csv file
combined_stats.to_csv (r'/home/jordysjoint/sp500/export_new_sp.csv', index = False, header = True)



