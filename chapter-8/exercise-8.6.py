# Chapter 8
# exercise 8.6
# ----------------------------------------------------------
# error checking - use try/except to catch non-numeric input,
# entered code to check and prevent duplicate number in list,
# if number exist in list,
# print message asking for a new number

num_list = list()

while True:
	inp_num = input("Enter a number: ")
	
	if inp_num == "done":
		break
		
	try:
		value = float(inp_num)
	except:
		print("You have entered a string! Please enter number.")
		continue
	
	if not value in num_list:
		num_list.append(value)
	else:
		print("Number already in list.")
		continue
	
print("Maximum:",max(num_list))
print("Minimum:",min(num_list))



