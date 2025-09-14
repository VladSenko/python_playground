# combine two dataframes

combined = pd.concat([df1, df2], axis=0)  # combine data along rows
combined = pd.concat([df1, df2], axis=1)  # combine data along columns


# merge two data sets using a column name as a key (this column shuld exist in both data frames)
merged = pd.merge(df1, df2, on='common_column')


# makes a left join
merged = pd.merge(df1, df2, how='left', on='common_column')


# makes an inner join
merged = pd.merge(df1, df2, how='inner', on='common_column')


# join data using index alignment, regardless of column name
joined = df1.join(df2, how='inner')
