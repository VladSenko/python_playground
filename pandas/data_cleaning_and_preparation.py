

df = df.dropna()
df = df.dropna(axis=1)  # drop columns with missing values


# fill specific column missing values with specific value
df['column_name'] = df['column_name'].fillna(0)


df.fillna(method='ffill')
df.fillna(method='bffill')

# fill missing values in specific column by interpolation method
df['column_name'] = df['column_name'].interpolate()
