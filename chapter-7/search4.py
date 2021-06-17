# chapter 7
# searching through a file

fhandle = open('mbox-short.txt')
count = 0

for line in fhandle:
	line = line.rstrip()
	if line.find('@uct.ac.za') == -1:
		continue
		
	print(line)
	
