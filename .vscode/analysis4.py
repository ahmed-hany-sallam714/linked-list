
import pandas as pd 
import numpy as np
people= pd.read_csv("diabetes.csv")

print(people.head())
print(people.info())
print(people.describe())
print(people.isnull().sum())
print(people["Outcome"].value_counts().sort_values(ascending=False))
for column in people.columns :
    print(f"the mean value for {column} is {round(people[column].mean())}")
for column in people.columns :
    print(f"the std for {column} is {round(people[column].std())}")
for column in people.columns :
    print(f"the median for {column} is {round(people[column].median())}")
for column in people.columns :
     print(f"the mean value for {column} is {round(np.mean(people[column]))}")
for column in people.columns :
    print(f"the std for {column} is {round(np.std(people[column]))}")
print(people.loc[people["Outcome"] == 1 , : ])
print(people.loc[people["Outcome"] == 0 , : ])
print((people["BMI"] == 0).any())
print((people["BloodPressure"] == 0).any())



