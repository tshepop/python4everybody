import socket

"""
Change the socket program socket1.py to prompt the user for the
URL so it can read any web page. You can use split(’/’) to break the URL into
its component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user
enters an improperly formatted or non-existent URL.

Sample Data: romeo.txt
"""

try:
    user_url = input("Enter url - ")
    hostname = user_url.split("/")
    # print(host)
    HOST = hostname[2]
    PORT = 80

    # For testing purposes using http.server

    # user_url equals to http://0.0.0.0/romeo.txt
    # hostname = user_url.split("/")
    # HOST = hostname[2]
    # PORT = 8000
    # web_resource = hostname[3]

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((HOST, PORT))
    # cmd = "GET " + web_resource + " HTTP/1.0\r\n\r\n" use this line only with localhost
    cmd = "GET " + user_url + " HTTP/1.0\r\n\r\n"
    my_sock.sendall(cmd.encode())

    while True:
        data = my_sock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())

    my_sock.close()

except:
    print("Check web-address is incorrect or does not exist.")
