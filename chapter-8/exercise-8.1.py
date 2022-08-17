# Chapter 8 List
# chop function

def chop(arr):
	"""
	function takes a list and modifies it,
	removing the first and last elements, returns None
	"""
	
	del arr[0]
	del arr[-1]
	
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
show_days = chop(weekdays)
print(weekdays)
print(show_days)
