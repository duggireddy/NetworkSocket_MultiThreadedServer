import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((socket.gethostname(), 1234))

except socket.error as e:
    print(str(e))


while True:

    respose = client_socket.recv(1024)

    if not respose:
        client_socket.close()

    print(respose.decode("utf-8"))

client_socket.close()














'''
payload = "Hey Server"

try:
    while True:
        client_socket.send(payload.encode("utf-8"))
        data = client_socket.recv(1024)
        print("timestamps: ",data.decode("utf-8"))
      
except KeyboardInterrupt:
    print("Exited by user")
client_socket.close()
'''
       

