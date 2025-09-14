df = df.rename(columns={'old_name': 'new_name'})  # rename data frame column


# change data frame column values type
df['column_name'] = df['column_name'].astype('float')

# convert string values to dateTime values
df['column_name'] = pd.to_datetime(df['column_name'])


# create a new column by modification of existing column
df['new_column'] = df['existing_column'] * 2
