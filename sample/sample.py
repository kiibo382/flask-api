#%%
for i in range(1, 5):
  print(i)



print('####################')



for i in reversed(range(5)):
  print(i)



print('####################')



arr1 = []
for i in range(5):
  arr1.append(int(input()))
  
sum = 0
for i in arr1:
  sum += i

print(sum)



print('######################')



import random

arr2 = []
for i in range(5):
  arr2.append(random.uniform(-10, 10))

sort_arr2 = sorted(arr2, key=abs, reverse=True)

print(sort_arr2)



print('########################')



tmp = 'ABCDEF'
tmp_split = list(tmp)
print(tmp_split)
print(tmp_split[1])
print(tmp_split[4])
print(''.join(tmp_split))

print(tmp[1])
print(tmp[4])
#%%