#%%
import random

with open('sample.csv', 'w') as f:
  for i in range(20):
    rand = random.uniform(1, 6)
    f.write(str(rand) + '\n')



import numpy as np

arr1 = np.array([[1,2],
                 [3,4],
                 [5,6]])
print(arr1.shape)

# 1行目の2列目
print(arr1[0, 1])

# 1行目以降の2列目
print(arr1[:, 1])

arr2 = np.arange(20)
print(arr2)

# reshapeに-1を使用すると自動で決定してくれる
reshape_arr2 = arr2.reshape(-1, 1)
print(reshape_arr2)

#%%