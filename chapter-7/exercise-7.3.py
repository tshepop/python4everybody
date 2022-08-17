# Chapter 7
# exercise 7.3

f_inp = input("Enter the filename: ")

try:
	fhand = open(f_inp)
	
except:
	
	if f_inp == "na na boo boo":
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
	else:
		print("File cannot be opened:", f_inp)
	exit()

count = 0

for line in fhand:
	if line.startswith("Subject:"):
		#print(line)
		count = count + 1
		
print("There were",count,"subject lines in "+ f_inp)
#print("lines:",count)
