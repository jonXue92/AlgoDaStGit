def sum1(arr):
	result=0
	if len(arr)==0:
		result=0
	else:
		result=arr.pop(0)+sum1(arr)
	return result

print(sum1([]))
print(sum1([6]))	
print(sum1([1,2,3,4,5]))