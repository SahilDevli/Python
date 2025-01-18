# Series VS DataFrame

import pandas as pd
import numpy as np

df = pd.read_csv("demo2.csv")
# print(df)

# differenece of  series and data frames

ser = pd.Series(np.random.rand(10))
print(ser)

print('type : ',type(ser))


df = pd.DataFrame(np.random.rand(10,5), columns=['A','B','C','D','E'])
print(df)

print('type : ',type(df))

