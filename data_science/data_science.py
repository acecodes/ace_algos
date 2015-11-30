import numpy as np
import pandas as pd

# Create a series of values with an integer index
series = pd.Series([1, 3, 5, np.nan, 6, 8])

print(series)

# Create date ranges
monthly_dates = pd.date_range('20150801', periods=4, freq='M')
daily_dates = pd.date_range('20150925', periods=4, freq='D')

print(monthly_dates)
print(daily_dates)

# Create labeled data (data frames) with random records
df_monthly = pd.DataFrame(np.random.randn(4, 4),
                          index=monthly_dates,
                          columns=list('ABCD'))
df_daily = pd.DataFrame(np.random.randn(4, 4),
                        index=daily_dates,
                        columns=list('EFGH'))

print(df_monthly)
print(df_daily)

# Using a dict to construct a DataFrame
dataframe_2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20150505'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', ' test', 'train']),
    'F': 'Testing'
})

print(dataframe_2)
print(dataframe_2.dtypes)

print('Dataframe head (two elements):')
print(dataframe_2.head(2))
print('Dataframe tail (two elements):')
print(dataframe_2.tail(2))
print('Dataframe stats:')
print(dataframe_2.describe())
print('Dataframe transposition:')
print(dataframe_2.T)

test_index = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print('Another series (test_index):')
print(test_index)

print('Index of test_index:')
print(test_index.index)

print('Create series from a dictionary:')
dic1 = {'a': 1, 'b': 2, 'c': 3}
dict_series = pd.Series(dic1)
print(dict_series)

print('Series from dictionary with an arbitrary index:')
dict_series_2 = pd.Series(dic1, index=['a', 'b', 'c', 'd'])
print(dict_series_2)
print('NaN is standard in Pandas for missing data!')
