# Chapter 7
# reading files
# count the lines of the text file
# print output using different ways - for my learning

fhand = open('mbox-short.txt')
count = 0

for line in fhand:
	count = count + 1
	
#print('Lines count is', count, 'in the file')
#result = f"Lines count: {count}"
#result = "Lines count: {}".format(count)
result = "Lines count: %d" % (count)
print(result)