# Chapter 8
# exercise 8.4

fname = input("Enter a file name: ")
fhand = open(fname)
lst = list()


for line in fhand:
	line = line.rstrip()
	print(line)
	words = line.split(" ")
	#print(words)
	for char in words:
		#print(char)
		if not char in lst:
			lst.append(char)
		lst.sort()

print()
print(lst)