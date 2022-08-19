import socket

"""
Change your socket program so that it counts the number of characters it has received
and stops displaying any text after it has shown 3000 characters.The program should retrieve
the entire document and count the total number of characters
and display the count of the number of characters at the end of the
document.

sample data: romeo-full.txt
"""

try:

    user_input = input("Enter url: ")
    host = user_input.split("/")

    HOST = host[2]

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((HOST, 80))
    sock_command = "GET " + user_input + " HTTP/1.0\r\n\r\n"
    my_sock.sendall(sock_command.encode())

    count = 0
    # bytes variable to store data from socket, and be able to access that data outside the loop.
    retrieve_char = b""

    while True:
        data = my_sock.recv(512)
        if (len(data) < 1):
            break

        retrieve_char += data
        count = count + len(data)

        # print(type(retrieve_char))  # verify if variable still holds bytes data

        # retrieve_char = retrieve_char[:500]
        # retrieve_char = retrieve_char[:1500]
        retrieve_char = retrieve_char[:3000]

    print(retrieve_char.decode().strip())
    print()
    print("Retrived Characters:", len(retrieve_char))
    print("Total document characters:", count)

    my_sock.close()

except:
    print("The web-address is incorrect or does not exist.")
