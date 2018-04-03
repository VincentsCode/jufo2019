import socket
import Constants

# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 1337))

socket.listen(1)

connection, client_address = socket.accept()
print('connection from', client_address)
while True:
    data = connection.recv(16)
    msg = str(data, "utf8")
    msg = msg.replace("#", "")
    print(msg)
    connection.sendall(bytes(Constants.ANSWER_POSITIVE, "utf8"))
