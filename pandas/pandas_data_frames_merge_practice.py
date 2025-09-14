import pandas as pd
import numpy as np


df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})


df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Score': [85, 90, 88]
})


print('Data Frame 1: \n', df1)
print('Data Frame 2: \n', df2)


merged = pd.merge(df1, df2, how='inner', on='ID')
print('Merged: \n', merged)


merged['Score_percentage'] = (merged['Score'] / 100) * 100
print('Transformed data set: \n', merged)
