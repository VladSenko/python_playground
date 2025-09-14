import pandas as pd

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

# load dataset

df = pd.read_csv(url)

# Explore the structure
# print("first 5 rows: \n", df.head())
# print("last 5 rows: \n", df.tail())

# print(df.describe())

selected_columns = df[['species', 'sepal_length']]
# print("selected cols: \n", selected_columns)

filtered_rows = df[(df['sepal_length'] > 5.0) & (df['species'] == 'setosa')]
print('Filtered rows: \n', filtered_rows)
