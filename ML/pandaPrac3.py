# more functions and basic syntax

import pandas as pd
import numpy as np

df  = pd.DataFrame(np.random.rand(10,5))  # create random value table/data_freame of 10 rows and 5 columns.
# print(df)

print(df.index) #give information about indexes

df.columns = ['A', 'B', 'C', 'D', 'E'] # change column names
print(df)

print(df.T) # do Transpose of matrix

print(df.sort_index(axis=0,ascending=False)) # sort in descending order of row names
print(df.sort_index(axis=1,ascending=True)) # sort in ascending order of column names


new=df # create a view of data frame (or some times copy)

new_copy = df.copy() # make a copy of data set in 'var_name':'new_copy'

new_copy.loc[0,0] = 100 # change value in a specific cell  


# drop rows or columns
# df.drop(0, axis=0, inplace=True) # remove row at index 0
# df.drop('A', axis=1, inplace=True) # remove column 'A'