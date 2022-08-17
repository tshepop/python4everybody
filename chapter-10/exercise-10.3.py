# Chapter 10
# exercise 3

import string

file_name = input("Enter the file name: ")
try:
	file_open = open(file_name)
except FileNotFoundError:
	print("File is not available", file_name)
	exit()
	
freq_dic = dict()
count = 0

for line in file_open:
	line = line.translate(str.maketrans("", "", string.punctuation))
	line = line.translate(str.maketrans("", "", string.digits))
	line = line.lower()
	words = line.split()
	
	for word in words:
		for letter in word:
			#print(letter)
			count += 1
			if letter not in freq_dic:
				freq_dic[letter] = 1
			else:
				freq_dic[letter] += 1

letter_lst = list()

for key, val in freq_dic.items():
	#print(val, key)
	letter_lst.append((val,key))
	
letter_lst.sort(reverse=True)
letter_pct = 0

for val, key in letter_lst:
	#print(val, key)
	print(val / count, key)
	
#print(letter_lst)
#print(freq_dic)
#print(count)
