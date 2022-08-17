# Chapter 9
# exercise 3
# dataset or input data from mbox-short.txt

f_name = input("Enter the file name: ")
try:
	f_hand = open(f_name)
except:
	print("File cannot be opened.", f_name)
	exit()
	
d = dict()

count = 0

for line in f_hand:
	line = line.rstrip()
	words = line.split()
	if len(words) == 0:
		continue
		
	if words[0] != "From":
		continue
	
	#count = count + 1
	#print(words[1])
	
	if words[1] not in d:
		d[words[1]] = 1
	else:
		d[words[1]] += 1
		
#for key in d:
#	print(key, d[key])
	
print(d)

