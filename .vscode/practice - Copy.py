
import pandas as pd 
import numpy as np

sales= pd.read_csv("sales_train.csv")
'''
print(sales["shop_id"].isnull().sum())
print(sales.head())

#print(f"the market which sold the biggest quantity is {}")
'''
x=sales.groupby("shop_id")["item_cnt_day"].sum().max()["shop_id"]
#print(f"the market which sold the biggest quantity's id is {} ")


