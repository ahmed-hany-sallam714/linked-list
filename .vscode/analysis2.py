
import pandas as pd 
import numpy as np
people= pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")
people=people.dropna()
print(people.head())
print(round(people["Weight"].mean()))
print(round(people["Height"].mean()))
print(people.groupby("Gender")["Height"].mean())
print(people.groupby("Gender")["Weight"].mean())
def filter_func (dataframe) :
    return dataframe["Weight"] <  dataframe["Weight"].mean()
print(people.groupby("Gender").filter(filter_func))
#print(sales.groupby("PRODUCT")["SALES"].sum())
#print(sales.isnull().sum())
#print(sales.shape)

'''
🛠 تنفع تعمل بيها إيه بالمكتبتين؟
تحسب متوسط الوزن والطول باستخدام NumPy.

تصنف الأشخاص حسب الجنس أو الـ BMI باستخدام Pandas groupby.

تطلع مثلاً من أكتر فئة موجودة: النحاف؟ الوزن الطبيعي؟ البدناء؟

تشوف الطول والوزن المتوسط لكل جنس.

تطبق فلترة (زي استخراج الناس اللي وزنهم فوق المتوسط).

تستخدم عمليات رياضية بسيطة زي الفرق بين الوزن والطول (لو حابب).

'''