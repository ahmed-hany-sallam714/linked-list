import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic.head())
print(titanic.pivot_table(index=["sex","who"],values=["age","fare"],
aggfunc={"age":"mean","fare":"median"},columns=["class","alive"]))









'''

df = pd.DataFrame({"key":["A","B","D","A","B","D"],"data1":[1,2,3,4,5,12] , "data2" : [6,7,8,9,10,15]})
def apply_func(dataframe):
    dataframe=dataframe["data1"]/dataframe["data1"].mean()
    return dataframe
print(df.groupby("key").apply(apply_func))


for (x,y) in data:
    print(x)
    print(y)
print(df.groupby("key").aggregate([np.mean]))
print(df.groupby("key").aggregate({"data1":np.mean, "data2":np.max}))
def filter_func (dataframe) :
    return dataframe["data1"].mean()<5 
print(df.groupby("key").filter(filter_func))
def transform_func (dataframe) :
    dataframe=dataframe-dataframe.mean()
    return dataframe
print(df.groupby("key").transform(transform_func))
'''
