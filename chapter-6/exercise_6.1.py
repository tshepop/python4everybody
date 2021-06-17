# Exercise 1
# Traversal through a string with a loop
 
fruit = 'banana'
last = len(fruit)
index = 0
 
while last > index:
	letter = fruit[last-1]
	print(letter)
	last = last - 1
	