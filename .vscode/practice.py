
import pandas as pd
import numpy as np
df=pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
df.info()
data=df.iloc[:,-3:].values
print(data.size)
print(data.ndim)
print(data.shape)
print(data.dtype)
#print(data[ : , 2:])
#print(data[ : :3])
#print(data[ : , : :2])
col1 = data[ : , 0].reshape(-1,1)
col3 = data[:,2].reshape(-1,1)
#print(np.hstack((col1,col3)))
#print(data[::-1])
#print(data[::, : :-1])
#print(f"the maximum heigth is {np.max(data[:,0])}")
#print(f"the minimum heigth is {np.min(data[:,0])}")
#print(f"the maximum weigth is {np.max(data[:,1])}")
#print(f"the minimum weigth is {np.min(data[:,1])}")
#print(f"the mean value for the heigth is {round(np.mean(data[:,0]))}")
#print(f"the std for the heigth is {round(np.std(data[:,0]))}")
#print(f"the mean value for the heigth is {round(np.sum(data[:,0])/data[:,0].size)}")
#s =0
#for i in range(data[:,0].size):
    #x = np.pow(data[:,0][i]-np.mean(data[:,0]),2)
    #s+=x

#print(f"the std for the heigth is {np.sqrt(s/np.size(data[:,0])-1)}")
#print(f"the mean value for the weigth is {round(np.mean(data[:,1]))}")
#print(f"the std for the heigth is {round(np.std(data[:,1]))}")
#print(f"the mean value for the weigth is {round(np.sum(data[:,1])/np.size(data[:,1]))}")
#weigth = np.pow(data[:,1]-np.mean(data[:,1]),2)
#weigths=np.sum(weigth)
#sdd=np.sqrt(weigths/(np.size(data[:,1])-1))
#print(f"the std for the heigth is {round(np.std(data[:,1]))}")
#print(np.percentile(data[:,0],75))
#print(np.median(data[:,0]))
#print((data[:,0]-np.mean(data[:,0]))/np.std(data[:,0]))
#print((data[:,0]-np.min(data[:,0]))/(np.max(data[:,0])-np.min(data[:,0])))
#print(np.argmax(data[:,0]))
#===============
x = data[:,0]**2
reshapedx=x.reshape(-1,1)
date=np.concatenate((data,reshapedx) ,axis = 1)
print(data)
#==================
#rootedx =np.sqrt(data[:,0])
#rootedy =np.sqrt(data[:,1])
#print(rootedx.reshape(-1,1))
#print(rootedy.reshape(-1,1))


