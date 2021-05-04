# Chapter 8
# Debugging
# exercise 2

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	print("Enter correct file name.")
	exit()

for line in fhand:
	words = line.split()
	#print("Debug >",words)
	
	if len(words) == 0:
		continue
		
	if words[0] != "From":
		continue
		
	print(words[2])