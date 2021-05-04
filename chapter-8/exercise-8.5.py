# Chapter 8
# exercise 8.5

fname = input("Enter a file name: ")
fhand = open(fname)
count = 0

for line in fhand:
	line = line.rstrip()
	if not line.startswith("From "):
		continue
	
	words = line.split()
	print(words[1])
	count = count + 1
	#print(line)
	
#print("Line count", count)
print()
print("There were", count, "lines in the file with From as the first word")