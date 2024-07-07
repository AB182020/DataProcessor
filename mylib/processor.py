import pandas as pd


def customFilterByCol(df, cols):
    cus_filter = df.filter(items=cols)
    return cus_filter


def customFilterByRegex(df, pattern, ax):
    cus_filter = df.filter(regex=pattern, axis=ax)
    return cus_filter


def customLoc(df, col, condition):
    return df.loc[df[col] < condition]


def customQuery(df, year=None, artist=None, track=None):
    query = df

    if year is not None:
        query = query[query['Year'] == year]

    if artist is not None:
        query = query[query['Artist'] == artist]

    if track is not None:
        query = query[query['Track'] == track]

    # if query.empty:
    #     print("No results found for the given criteria.")
    # else:
    #     print(query)
    return query

# customQuery(df, 1992)
# customQuery(df, artist='Usher')
# customQuery(df, year=1996, artist='Spice Girls', track='Wannabe')

# cols_to_select = ['Artist', 'Track', 'Year']
# print(customFilter(df, cols_to_select))
# cols_to_select = ['streams_mnth', 'Year', 'strms_min']
# print(customFilter(df, cols_to_select))
# print(df.head(4))
# print(df.tail(6))
