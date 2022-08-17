# chapter 7
# exercise 7.1

fname = input('Enter a file name: ')

fhand = open(fname)

count = 0

for line in fhand:
	line = line.upper().strip()
	print(line)
