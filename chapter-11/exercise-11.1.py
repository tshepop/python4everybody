# chapter 11
# exercise 1 
# simulate the operation of the grep command

import re

inp_expr = input("Enter a regular expression: ")
file_name = "mbox.txt"
try:
	file_handle = open(file_name)
except FileNotFoundError:
	print("File not available.", file_name)
	exit()
	
counter = 0

for line in file_handle:
	line = line.rstrip()
	if re.search(inp_expr, line):
		counter += 1
		
print(f"{file_name} had {counter} lines that matched {inp_expr}")
