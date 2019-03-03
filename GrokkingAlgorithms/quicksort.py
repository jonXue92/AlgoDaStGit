def quicksort(array):
	if len(array)<2:
		return array
	else:
		pivot=array[0]
		less=[x for x in array[1:] if x<=pivot]
		greater=[x for x in array[1:] if x>pivot]
		return quicksort(less)+[pivot]+quicksort(greater)
		
print(quicksort([10,5,2,3]))