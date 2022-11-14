
import os
import pandas as pd
import akshare as ak
import mplfinance as mpf

def get_stock_data():
    # stock_us_daily_df = ak.stock_us_daily(symbol="AAPL", adjust="qfq")
    # stock_us_daily_df = stock_us_daily_df[["open", "high", "low", "close", "volume"]]
    # stock_us_daily_df.columns = ["Open", "High", "Low", "Close", "Volume"]
    # stock_us_daily_df.index.name = "Date"
    # print(stock_us_daily_df)
    # stock_us_daily_df = stock_us_daily_df["2020-04-01": "2020-04-29"]
    # mpf.plot(stock_us_daily_df, type='candle', mav=(3, 6, 9), volume=True, show_nontrading=False)
    # stock_us_daily_df = ak.stock_us_daily(symbol='AAPL',adjust='qfq')
    # stock_us_daily_df = stock_us_daily_df[['open','high','low','close','volume']]
    # stock_us_daily_df.columns = ['open','high','low','close','volume']
    # stock_us_daily_df.index.name = 'Date'
    # stock_us_daily_df = stock_us_daily_df['2020-04-01':'2020-04-29']
    # mpf.plot(stock_us_daily_df,type = 'candle',mav=(3,6,9),volume= True,show_nontrading= False)
    # print(stock_us_daily_df)
    stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol='sz399006')
    stock_zh_index_daily_df = stock_zh_index_daily_df[["date","open", "high", "low", "close", "volume"]]
    stock_zh_index_daily_df.columns = ["Date","Open", "High", "Low", "Close", "Volume"]
    # stock_zh_index_daily_df.index.name = "Date"
    # stock_zh_index_daily_df = stock_zh_index_daily_df.reset_index()

    # mpf.plot(stock_zh_index_daily_df,type = 'candle',mav=(3,6,9),volume= True,show_nontrading= False)
    print(stock_zh_index_daily_df)
    
    
    pass

def show_stock_data_as_candle(df: pd.DataFrame):
    pass

def main():
    get_stock_data()
    pass

if __name__ == '__main__':
    main()