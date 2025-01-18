# basic syntax and function

import pandas as pd
import numpy as np

dic = {
    'file_path': ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt'],
    'file_size': [1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(dic)  # create dataframe/table from dictionary
print(df)

array = df.to_numpy() # convert to numpy array format
print(array)

df.index = [1,2,3,4,5] # give this value to index
df.to_csv("demo.csv") # convert to CSV format in new file demo.csv

print(df.describe())   # statistical analysis of dataFrame
print(df.head(2))       # print starting rows
print(df.tail(2))   # print ending rows