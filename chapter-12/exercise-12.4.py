import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

"""
Change the urllinks.py program to extract and count paragraph (p)
tags from the retrieved HTML document and display the count of the paragraphs
as the output of your program. Do not display the paragraph text, only count
them. Test your program on several small web pages as well as some larger web
pages.

install BeautifulSoup or download bs4 folder
"""
count = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user_url = input("Enter Web Address: ")
user_html = urllib.request.urlopen(user_url, context=ctx).read()
soup = BeautifulSoup(user_html, "html.parser")


for tag in soup.find_all("p"):
    # print(tag)
    count = count + 1

print("Number of tags", count)