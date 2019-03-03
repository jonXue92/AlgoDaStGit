#map
arr1=[1,2,3,4,5]
arr2=map(lambda x:2*x, arr1)
print(list(arr2))
from functools import reduce
print(reduce(lambda x,y:x+y, arr1))