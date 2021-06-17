# Chapter 5
# exercise 5.2
# program that prompts for a list of numbers
# and at the end prints out both the maximum and minimum of the numbers

#count = 0
#total = 0
numbers = list()

while True:
	line = input('Enter a number: ')
	try:
		line = int(line)
		#count = count + 1
		#total = total + line
		#average = total / count
		numbers.append(line)
		
	except ValueError:
		if line == 'done':
			break
		else:
			print('Invalid data')

print("Maximum: " + str(max(numbers)))
print("Minimum: " + str(min(numbers)))
