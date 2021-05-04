# chapter 8
# Debugging
# exercise 3
# ------------------------------------------------

fname = input("Enter a file name: ")
try:
	fhand = open(fname)
except:
	print("Enter correct file name.")
	exit()

for line in fhand:
	words = line.split()
	#print("Debug >",words)
	# guardian code - skip if first word is empty
	if len(words) == 0 or words[0] != "From":		
		continue
		
	print(words[2])