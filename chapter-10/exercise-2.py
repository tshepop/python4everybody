# Chapter 10
# exercise 2

file_name = input("Enter the file name: ")
try:
	file_handle = open(file_name)
except FileNotFoundError:
	print("File not available.")
	quit()
	
d_time = dict()

for line in file_handle:
	words = line.split()
	#print(words)
	if len(words) == 0:
		continue
	
	if words[0] != "From":
		continue
	
	#print(words[5])
	hr = words[5].split(":")
	#print(hr[0])
	if hr[0] not in d_time:
		d_time[hr[0]] = 1
	else:
		d_time[hr[0]] += 1

hr_lst = list()

for hours, count in d_time.items():
	hr_lst.append((hours, count))

#print(hr_lst)
hr_lst.sort()

for hours, count in hr_lst:
	print(hours, count)

#print(hr_lst)
#print(d_time)
