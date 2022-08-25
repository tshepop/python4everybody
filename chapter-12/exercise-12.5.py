import socket
import ssl

"""
(Advanced) Change the socket program so that it only shows data
after the headers and a blank line have been received. Remember that recv is
receiving characters (newlines and all), not lines

sample data: romeo.txt, romeo-full.txt
"""

user_url = input("Enter web address: ")
hostname = user_url.split("/")
HOST = hostname[2]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((HOST, 80))
get_cmd = "GET " + user_url + " HTTP/1.0\r\n\r\n"
my_sock.sendall(get_cmd.encode())

lines = b""

while True:
    data = my_sock.recv(512)
    if(len(data) < 1):
        break
    # print(data.decode())
    lines = lines + data

my_sock.close()

# find lines following the header
pos = lines.find(b"\r\n\r\n")
# print("Header:", pos)
# print(lines[:pos])
lines = lines[pos+2:].decode()
print(lines)
