import numpy as np 
import pandas as pd

# 1. تحميل البيانات
data = pd.read_csv("supermarket_sales - Sheet1.csv") 

# 2. استكشاف مبدئي للبيانات
print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())
print(data.columns)

# 3. تحليل حسب الفروع
print(data.groupby("Branch")["Total"].mean())    # متوسط المبيعات
print(data.groupby("Branch")["Total"].sum())     # إجمالي المبيعات
print(data["Branch"].value_counts())             # عدد الفواتير
print(data.groupby("Product line")["Quantity"].sum().sort_values(ascending=False))
print(data.groupby("Product line")["Total"].mean().sort_values(ascending=False))
print(data["Gender"].value_counts())
print(data.groupby("Gender")["Total"].mean().sort_values(ascending=False))

print(data["Payment"].value_counts().sort_values(ascending=False))
print(data["Payment"].value_counts().idxmax())

print(np.mean(data["Total"]))
print(np.std(data["Total"]))
print(np.min(data["Total"]))
print(np.max(data["Total"]))
