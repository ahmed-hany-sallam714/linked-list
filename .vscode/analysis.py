
import pandas as pd 
import numpy as np
sales= pd.read_csv("sales_train.csv")
items= pd.read_csv("items.csv")
shops= pd.read_csv("shops.csv")
item_categories= pd.read_csv("item_categories.csv")
data=pd.read_csv("Online_Retail.csv")
encoding=("ISO-8859-1")
'''
def filter_func (dataframe) :
    return dataframe["item_price"].mean()> 500
print(sales.groupby("item_price").filter(filter_func))


print(sales.aggregate({"item_price" : np.mean }))
#print(sales)
#print(sales.groupby("shop_id")["item_price"].mean())
#for (x,y) in sales.groupby("shop_id") :
 #   print(x)
  #  print(y)
'''





#print(sales["item_id"].std())
#print(sales["item_id"].count())
#print(sales["item_id"].mean())
#print(sales["item_id"].median())
#print(sales["item_id"].min())
#print(sales["item_id"].max())
#print(sales["item_id"].var())
#print(sales["item_id"].prod())
#print(sales["item_id"].sum())
#print(sales.describe())
#print(sales.groupby("item_id")["item_price"].mean())
#number=0
#for i in sales["item_cnt_day"] :
#    if i > 0:
#     number +=1
#print(f"the number of the sold things is {number}")
#print(pd.isnull(sales).sum())
#print(sales.merge(items,how="outer",on="item_price"))
#print(sales.head())
#print("*"*20)
#print(items.head())
#print("*"*20)
#print(shops.head())
#print("*"*20)
#print(item_categories.head())
#print("*"*20)
#a = pd.DataFrame({"item" :["a","b","c" ] , "id" : [5,2,4] })
#b = pd.DataFrame({"item" :["f","8","c" ] , "id" : [1,2,3] })
#print(pd.merge(a,b,how="outer",on=["item","id"]))
#print(a._append(b))                
#a=a.set_index("id")
#b=b.set_index("id")
#print(a.join(b,how="outer",lsuffix="from_left",rsuffix="from right"))
#print(a)
#print(b)
#print(pd.merge(a,b,how="inner",on="id"))
#print(pd.merge(a,b,how="outer",on="id"))
#print(pd.merge(a,b,how="left",on="id",suffixes=("from left","from right")))
#print(pd.merge(a,b,how="outer",left_on="item",right_on="ho"))
#print(pd.concat([a,b]))
#print(pd.merge(a,b,how="inner",on="id").drop(columns="id"))
#print(pd.concat([a,b],keys=["x","y"]).reset_index())
#print(pd.concat([a,b],keys=["x","y"]))
#print(pd.concat([a,b],ignore_index=True))
