import pandas as pd

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df_ibov = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/%5EBVSP?period1=1674237073&period2=1705773073&interval=1d&events=history&includeAdjustedClose=true')
df_reversed = df_ibov.iloc[::-1]

