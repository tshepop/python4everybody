# chapter 7
# searching through a file
# use the try/catch

fname = input('Enter the file name: ')

try:
	fhand = open(fname)
except:
	print('File does not exist:', fname)
	exit()
	
count = 0

for line in fhand:
	line = line.rstrip()
	if line.startswith('Subject'):
		count = count + 1
		
print('There were',count, 'subject lines in', fname)

