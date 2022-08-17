# Chapter 9
# exercise 5
# dataset or input data from mbox-short.txt
# This program records the domain name (instead of the address) where,
# the message was sent from instead of who the mail came from

f_name = input("Enter the file name: ")
try:
	f_handle = open(f_name)
except FileNotFoundError:
	print("File cannot be opened.", f_name)
	exit()
	
d_domain = dict()

for line in f_handle:
	words = line.split()
	#print(words[1])
	if len(words) == 0:
		continue
	
	if words[0] != "From":
		continue
		
	#print(words[1])
	domain = words[1].split("@")
	#print(domain[1])
	if domain[1] not in d_domain:
		d_domain[domain[1]] = 1
	else:
		d_domain[domain[1]] += 1
		
print(d_domain)
