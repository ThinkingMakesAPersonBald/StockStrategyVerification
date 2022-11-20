'''
First step：Get stock data from net work and save in location, stock data and 汇率数据
Second step: 分析股票和汇率数据的相关性
Third step: stock and 汇率 相关性数据图形化展示
'''


import os
import pandas as pd
import akshare as ak
import mplfinance as mpf

root_path = '/Users/peixinhua/Desktop'
output_folder = 'stock data analysis'


'''
description: get stock history data by stock symbol
param {str} stock_symbol stock code
return {*}
'''
def get_stock_data(stock_symbol:str):
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
    
    # stock_zh_index_daily_df = stock_zh_index_daily_df[["date","open", "high", "low", "close", "volume"]]
    # stock_zh_index_daily_df.columns = ["Date","Open", "High", "Low", "Close", "Volume"]
    # stock_zh_index_daily_df.index.name = "Date"
    # stock_zh_index_daily_df = stock_zh_index_daily_df.reset_index()

    # mpf.plot(stock_zh_index_daily_df,type = 'candle',mav=(3,6,9),volume= True,show_nontrading= False)
    stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol='sz399006')
    print(stock_zh_index_daily_df)
    save_to_local_file(stock_zh_index_daily_df,'')
    pass
'''
description: get all stock or index code and name
return {*}
'''
def get_stock_index_spot():
    stock_zh_index_spot_df = ak.stock_zh_index_spot()
    print(stock_zh_index_spot_df)
    save_to_local_file(stock_zh_index_spot_df,'')

def show_stock_data_as_candle(df: pd.DataFrame):
    pass
'''
description: save type of pandas data frame data to local file
param {pd} df original data
param {str} file_name local file name
return {*}
'''
def save_to_local_file(df:pd.DataFrame,file_name:str):
    direction = os.path.join(root_path,output_folder)
    if not os.path.exists(direction):
        os.makedirs(direction)
    save_route = os.path.join(direction,file_name)
    df.to_csv(save_route)

def main():
    get_stock_index_spot()
    # 'sh000001'：上证指数'sz399006'深证实数'sz399006'创业板指
    index_name_list = ['sh000001','sz399006','sz399006'] 
    for code in index_name_list:
        get_stock_data(stock_symbol= code)
    pass

if __name__ == '__main__':
    main()