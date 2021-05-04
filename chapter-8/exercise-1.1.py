# Chapter 8 List
# middle function

def middle(arr):
	"""
	function that takes a list and returns a new list,
	that contains all but the first and last elements
	"""
	numlist = arr[1:]
	numlist = numlist[:-1]
	
	return numlist
	
numbers = [1, 2, 3, 4, 5]
nums = middle(numbers)
print(nums)