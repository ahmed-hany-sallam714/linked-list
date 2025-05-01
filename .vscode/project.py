import numpy as np
import pandas as pd
import seaborn as sns
data = pd.read_csv("Online_Retail.csv", encoding="ISO-8859-1")
data=data.dropna(subset="Description")
data=data.dropna(subset=["CustomerID"])
data = data[data["Quantity"] >= 0]
data ["TotalPrice"] = data ["Quantity"] * data ["UnitPrice"]
print(np.nansum(data))
'''
print(data.head())
print(data.groupby("CustomerID")["TotalPrice"].sum())

print(data.groupby("CustomerID")["Quantity"].sum())

print(data.shape)

print(data.isnull().sum())
]
print(data["Quantity"].dtype)
print(data["UnitPrice"].dtype)
print(data)
#print(data["Quantity"].value_counts())
'''

