# Chapter 5
# exercise 5.1
# - a program which repeatedly reads numbers 
# 	until the user enters done. 
# 	Once done is entered, print out the total, count, and average of the numbers

count = 0
total = 0

while True:
	line = input('Enter a number: ')
	try:
		line = int(line)
		
		count = count + 1
		total = total + line
		average = total / count
		
	except ValueError:
		if line == 'done':
			break
		else:
			print('Invalid data')
		
		
	#if line == 'done':
	#	break

	#count = count + 1
	#total = total + line
	#average = total / count
	#print(line)
	#print(line)

print(total, count, average)	

