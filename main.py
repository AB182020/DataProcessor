# This is a sample Python script.
import pandas as pd
import zipfile

from sqlalchemy import true

from mylib.processor import *
from mylib.DataAnalytics import *
import sqlalchemy as sal

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == "__main__":
    # load data from csv
    extract_zip_Fl('retailOrder.zip')
    df = pd.read_csv('orders.csv', na_values=['Not Available', 'Unknown'])
    # format data and derive columns
    clean_data(df)
    print(derive_cols(df))
    df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)
    print(df.columns)
    # load data to table
    loadDatatoDatabase(df, 'df_orders')
