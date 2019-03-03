def len1(arr):
	result=0
	if arr:
		arr.pop(0)
		result=1+len1(arr)
	return result

print(len1([]))
print(len1([6]))	
print(len1([1,2,3,4,5]))		