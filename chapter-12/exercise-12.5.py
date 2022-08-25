import socket

"""
(Advanced) Change the socket program so that it only shows data
after the headers and a blank line have been received. Remember that recv is
receiving characters (newlines and all), not lines

sample data: romeo.txt, romeo-full.txt
"""

user_url = input("Enter web address: ")
hostname = user_url.split("/")
HOST = hostname[2]

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((HOST, 80))
get_cmd = "GET " + user_url + " HTTP/1.0\r\n\r\n"
my_sock.sendall(get_cmd.encode())

lines = b""

while True:
    data = my_sock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())

my_sock.close()
