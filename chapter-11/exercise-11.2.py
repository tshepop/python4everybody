# chapter 11
# exercise 2
# extract the number from lines with - 'New Revision: 39722'
# using regular expression and findall method

import re

file_name = input("Enter file: ")
try:
	f_handle = open(file_name)
except FileNotFoundError:
	print("File not available.", file_name)
	exit()
	
counter = 0
revision_num = list()

for line in f_handle:
	line = line.rstrip()
	num = re.findall("New Revision: ([0-9]+)", line)
	if len(num) > 0:
		#print(num)
		revision_num.append(int(num[0]))
		counter += 1
		

result = sum(revision_num) / counter
print(f"{result:.7f}")
#print(result)
