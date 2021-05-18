# Chapter 9
# Exercise 2
# dataset or input data from mbox-short.txt

f_name = input("Enter the file name: ")

try:
	f_hand = open(f_name)
except:
	print("File cannot be opened.", f_name)
	exit()
	
days = dict()

for line in f_hand:
	line = line.rstrip()
	words = line.split()
	#print(words)
	
	if len(words) == 0:
		continue
		
	if words[0] != "From":
		continue
		
	#print(words[2])
	
	if words[2] not in days:
		days[words[2]] = 1
	else:
		days[words[2]] += 1
		
print(days)

