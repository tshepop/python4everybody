# chapter 10
# exercise 1

f_name = input("Enter the file name: ")
try:
	f_handle = open(f_name)
except FileNotFoundError:
	print("File cannot be opened.", f_name)
	exit()
	
d_mail = dict()

for line in f_handle:
	words = line.split()
	#print(words[1])
	if len(words) == 0:
		continue
	
	if words[0] != "From":
		continue
		
	#print(words[1])
	if words[1] not in d_mail:
		d_mail[words[1]] = 1
	else:
		d_mail[words[1]] += 1
		
comit_lst = list()

for email, count in d_mail.items():
	#print(email, count)
	comit_lst.append((count, email))

comit_lst.sort(reverse=True)

for count, email in comit_lst[:1]:
	print(email, count)
	
#print(comit_lst)
#print(d_mail)


