import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))

while True:
    respose = client_socket.recv(1024)
    print(respose.decode("utf-8"))

client_socket.close()













