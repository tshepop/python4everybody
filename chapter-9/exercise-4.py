# Chapter 9
# exercise 4
# dataset or input data from mbox-short.txt
# program to fugure out who has the most messages in the file.

f_name = input("Enter the file name: ")
f_hand = open(f_name)

d = dict()
largest = None
big_word = None

for line in f_hand:
	line = line.rstrip()
	words = line.split()
	
	if len(words) == 0:
		continue
		
	if words[0] != "From":
		continue
	
	#print(words[1])
	
	if words[1] not in d:
		d[words[1]] = 1
	else:
		d[words[1]] += 1
		
	for word, count in d.items():
		#print(word, count)
		if largest is None or count > largest:
			big_word = word
			largest = count
			
print(big_word, largest)

#print(d)
