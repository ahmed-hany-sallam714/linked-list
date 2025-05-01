
import pandas as pd
import numpy as np
df=pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
x =df.iloc[:,1:4]
print(x)
