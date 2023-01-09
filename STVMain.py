'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-11-14 10:20:53
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-01-09 23:03:15
FilePath: /StockStrategyVerification/STVMain.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import pandas as pd
import akshare as ak

output_file_name = '300750.xlsx'

def get_stock_history_data():
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol='300750',period='daily',start_date='20180611',end_date='20230109',adjust='')
    save_df_to_excel(stock_zh_a_hist_df)
    pass

def save_df_to_excel(df : pd.DataFrame):
    # get root path
    current_dir = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.join(current_dir,'output')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    df.to_excel(os.path.join(output_path,output_file_name),index= False)
    print('df save success !')
    pass

def main():
    get_stock_history_data()
    pass

if __name__ == '__main__':
    main()