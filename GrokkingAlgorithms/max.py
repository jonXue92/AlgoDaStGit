def max1(arr):
	num=arr.pop(0)
	if len(arr)==0:
		return num
	else:
		if num>=max(arr):
			return num
		else:
			return max(arr)
			
print(max1([6]))
print(max1([1,2,3,4,5]))
print(max1([100,1000,111]))