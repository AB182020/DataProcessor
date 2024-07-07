# This is a sample Python script.
import pandas as pd
from mylib.processor import *
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == "__main__":
    df = pd.read_csv('/Users/adarshbala/PycharmProjects/DataProcessor/TopSongs.csv')
    df1 = customQuery(df,1992)
    print(df1.head(5))
    df1 = customFilterByCol(df,['Track'])
    print(df1.head(5))
    df1 = customFilterByRegex(df,'^str',1)
    print(df1.tail(5))
    df1 = customLoc(df,'strms_hour',3.0)
    print(df1.head(4))

