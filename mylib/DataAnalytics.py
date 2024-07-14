import pandas as pd
import zipfile
import sqlalchemy as sal
from sqlalchemy import true


# zip_rf = zipfile.ZipFile('retailOrder.zip')
# zip_rf.extractall()
# zip_rf.close()

def extract_zip_Fl(filename):
    zip_rf = zipfile.ZipFile(filename)
    zip_rf.extractall()
    zip_rf.close()
    return zip_rf


def clean_data(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")
    return df


def derive_cols(df):
    df['discount'] = df['list_price'] * df['discount_percent'] * .01
    df['sale_price'] = df['list_price'] - df['discount']
    df['profit'] = df['sale_price'] - df['cost_price']
    return df


def connect():
    connection_string = 'mysql+mysqlconnector://root:Adarsh20#@localhost:3306/master'
    engine = sal.create_engine(connection_string)
    conn = engine.connect()
    return conn



def loadDatatoDatabase(df,table_name):
   conn = connect()
   df.to_sql(table_name,con=conn,index=False,if_exists='append')


