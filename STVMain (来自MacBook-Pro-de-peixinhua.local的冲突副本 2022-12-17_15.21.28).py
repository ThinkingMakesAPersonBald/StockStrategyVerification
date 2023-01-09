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
    stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol='sz399006')
    print(stock_zh_index_daily_df)
    save_to_local_file(stock_zh_index_daily_df,file_name= stock_symbol + '_index')
    pass
'''
description: get all stock or index code and name
return {*}
'''
def get_stock_index_spot():
    stock_zh_index_spot_df = ak.stock_zh_index_spot()
    print(stock_zh_index_spot_df)
    save_to_local_file(stock_zh_index_spot_df,file_name= 'stock_index_spot')

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
    save_route = os.path.join(direction,file_name + '.csv')
    df.to_csv(save_route)

def main():
    root_folder
    get_stock_index_spot()
    # 'sh000001'：上证指数'sz399006'深证实数'sz399006'创业板指
    index_name_list = ['sh000001','sz399006','sz399006'] 
    for code in index_name_list:
        get_stock_data(stock_symbol= code)
    pass

if __name__ == '__main__':
    main()