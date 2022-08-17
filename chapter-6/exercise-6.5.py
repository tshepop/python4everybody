# Exercise 6.5

# Use find and string slicing
# then use float function to convert extracted string

str = 'X-DSPAM_Confidence: 0.8475'
colpos = str.find(':')
extractedStr = str[colpos+1:]

convertToFloat = float(extractedStr)

print(colpos)
print(extractedStr)
print(convertToFloat)
print(type(convertToFloat))

