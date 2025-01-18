# Statistical functions for DataFrame

import pandas as pd
import numpy as np

df  = pd.DataFrame(np.random.rand(10,5))  # create random value table/data_freame of 10 rows and 5 columns.
# print(df)


print(df.sum(axis=0)) # sum of each column
print(df.sum(axis=1)) # sum of each row

print(df.mean(axis=0)) # mean of each column
print(df.mean(axis=1)) # mean of each row

print(df.max()) # maximum value in each column
print(df.min()) # minimum value in each column

print(df.var()) # variance of each column
print(df.std()) # standard deviation of each column

print(df.corr()) # correlation matrix of all columns

print(df.describe()) # statistical analysis of dataFrame
