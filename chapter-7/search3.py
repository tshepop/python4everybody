# chapter 7
# searching through a file

fhandle = open('mbox-short.txt')
count = 0

for line in fhandle:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	
	#print(line)
	count = count + 1
	print(count, line)
	
