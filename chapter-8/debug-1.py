# Chapter 8 
# Debugging
# exercise 1

fname = input("Enter a file name: ")
fhand = open(fname)

for line in fhand:
	words = line.split()
	#print("Debug >",words)
	
	if len(words) == 0:
		continue
		
	if words[0] != "From":
		continue
		
	print(words[2])