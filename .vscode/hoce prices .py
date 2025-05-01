import numpy as np 
sizes = np.array([10,11,12,13,14,15])
price = np.array([20,22,24,26,28,30])
m,b = np.polyfit(sizes,price,1)
print (m)
print(b)
size = int(input("please enter the size of your house :"))
print(f"the price for your house is {round(m*size+b)}")