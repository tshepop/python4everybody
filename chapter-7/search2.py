# chapter 7
# searching through file

fhandle = open('mbox-short.txt')
count = 0

for line in fhandle:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)