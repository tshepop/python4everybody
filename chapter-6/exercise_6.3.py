# Exercise 6.3

def count(str,char):
	word = str
	count = 0
	
	for letter in word:
		if letter == char:
			count = count + 1
	#print('Character:',char)
	return count
	
getLetter = count('banana', 'b')
#print('\n')
print('Total character in string:', getLetter)