import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
# print(df)

# load data from files
# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')

# wright data to file
# df.to_csv('data.csv', index=False)


# print(df.head())
# print(df.tail())
# print(df.info())
print(df.describe())

# selecting columns
print(df['Name'])

# select rows by filter
print(df[df['Age'] > 25])

# first row
print(df.iloc[0])

# first column
print(df.iloc[:, 0])

# select by label
print('By label', df.loc[0])
print('By label', df.loc[:, 'Name'])
