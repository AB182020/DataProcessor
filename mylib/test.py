import pandas as pd
from mylib.processor import *


def dataProcessor():
    df = pd.read_csv('/Users/adarshbala/PycharmProjects/DataProcessor/TopSongs.csv')
    print(customQuery(df, 1992))
