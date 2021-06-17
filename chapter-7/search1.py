# chapter 7
# searching through a file

fhandle = open('mbox-short.txt')
count = 0

for line in fhandle:
	if line.startswith('From:'):
		#print(line)
		count = count + 1
		print(count, line)
	
