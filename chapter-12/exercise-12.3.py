import urllib.request
import urllib.parse
import urllib.error
import ssl

"""
Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3) counting the
overall number of characters in the document. Don’t worry about the headers for
this exercise, simply show the first 3000 characters of the document contents.

sample data: romeo-full.txt
"""

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user_url = input("Enter url: ")
fhand = urllib.request.urlopen(user_url, context=ctx).read()

count = 0
words = b""

for line in fhand:
    count = count + 1

words = fhand.decode().rstrip()

char = words[:3000]  # number of characters to return
print(char)
print()
print(str(len(char)) + ": characters returned.")
