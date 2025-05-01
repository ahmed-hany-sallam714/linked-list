import numpy as np
x = np.array([[0,2,3,4],
              [0,6,7,8],
              [9,10,11,12]])
np.random.seed(73)
y=np.random.randint(20,size=(3,3))
print(np.count_nonzero(x))
print(np.sum(x<3,axis=0))
print(np.sum(x<3,axis=1))
print(np.count_nonzero(x<6))
print(x[x<5])