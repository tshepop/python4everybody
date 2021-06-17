# chapter 7
# searching through a file

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

#for line in fhand:
#	line = line.rstrip()
#	if line.startswith('From:'):
#		count = count + 1
#		print(count, line)
		
for line in fhand:
	line = line.rstrip()
	if line.startswith('Subject'):
		count = count + 1
		
print('There were',count, 'subject lines in', fname)

# use the try/catch