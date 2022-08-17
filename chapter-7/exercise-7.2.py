# Chapter 7
# excercise 7.2

fname = input('Enter the file name: ')
fhand = open(fname)

count = 0
total = 0

for line in fhand:
	if not line.startswith('X-DSPAM-Confidence:'):
		continue
		
	colpos = line.find(':')
	colstr = line[colpos+1:]
	convert_to_float = float(colstr)
		
	count = count + 1
	#print(line)
	
	#print(convert_to_float)
	total = total + convert_to_float
	#print(convert_to_float)
		
print('Average spam confidence:',float(total) /  float(count))		
print('Total',count)