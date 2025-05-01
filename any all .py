import numpy as np 
import pandas  as pd 
x = np.array ([1,-83,35,-46,78,np.nan])
#print(np.any(x>0,axis=0))
#print(np.all(x>0,axis=1))
#print(np.where(x>0,8,0))
#print(np.where(x>0))
#print(np.isnan(x))
print(np.savetxt("saved_arry.csv",x,delimiter=","))
print(np.isnan(x))