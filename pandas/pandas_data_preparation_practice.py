import pandas as pd
import numpy as np

# create a data set
data = {
    "Name": ['Alice', 'Bob', np.nan, 'David'],
    'Age': [25, np.nan, 30, 35],
    'Score': [85, 90, np.nan, 88]
}


df = pd.DataFrame(data)
print('Original data set: \n', df)


# fill the missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].interpolate()

print('Filled values: \n', df)


df = df.rename(columns={'Name': 'Student_name', 'Score': 'Exam_score'})
print('Renamed columns: \n', df)
