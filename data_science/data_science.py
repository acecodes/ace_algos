import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a series of values with an integer index
series = pd.Series([1, 3, 5, np.nan, 6, 8])

print(series)

# Create date ranges
monthly_dates = pd.date_range('20150801', periods=4, freq='M')
daily_dates = pd.date_range('20150925', periods=4, freq='D')

print(monthly_dates)
print(daily_dates)

# Create labeled data (data frames) with random records
df_monthly = pd.DataFrame(np.random.randn(4, 4), index=monthly_dates, columns=list('ABCD'))
df_daily = pd.DataFrame(np.random.randn(4, 4), index=daily_dates, columns=list('EFGH'))

print(df_monthly)
print(df_daily)
