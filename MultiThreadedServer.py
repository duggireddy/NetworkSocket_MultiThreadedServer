
import socket
import sys
import time
from datetime import datetime
from _thread import*

count =0
ThreadCount = 0 

#Creating Socket
try:
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #parameters(socketFamily, tcp=SOCK_STREAM and etc)
    print("socket connected")

except socket.error as err:
    print("Failed to create a socket")
    print("Reason" + str(err))
    sys.exit()

#Socket check with port 
try:
    target_host = socket.gethostname()
    traget_port = 1234
    socket_server.bind((target_host, traget_port))
    print("Socket connect to %s on port %s"%(target_host,traget_port))
    

except socket.error as err:
    print("Failed to connect to %s on port %d"%(target_host,traget_port))
    print("Reason: %s" %str(err))
    sys.exit()

socket_server.listen(5) 


def client_thread(connection):
    count =0

    while True:
        # get current datetime
        today = datetime.now()
        # Get current ISO 8601 datetime in string format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
        iso_date = today.isoformat()
        today = datetime.now()
        iso_date = today.isoformat()
        connection.send(str.encode("ISO DateTime: "+ iso_date))
        count = count+1
        if count == 10:
            print("Socket secession is ended")
            connection.close()
        time.sleep(5)


          


while True:
    client,address=socket_server.accept()
    print("Connected to "+address[0]+str(address[1]))
    start_new_thread(client_thread,(client,))
    ThreadCount+=1
    print("ThreadNumber"+str(ThreadCount))

socket_server.close()
























'''
        # get current datetime
        today = datetime.now()
        # Get current ISO 8601 datetime in string format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
        iso_date = today.isoformat()
        #print('ISO DateTime:', iso_date)

        print("server waiting for connection")
        client_socket, address = socket_server.accept() #it connects with the client 
        print(f"Connection from {address} has been established!")
        #clinentsocket.send(bytes(iso_date, "utf-8"))

        while True:
            #receiving data from client
            data = client_socket.recv(1024)
            if not data or data.decode("utf-8")=='END':
                break
            print("received from client client: %s "%data.decode("utf-8"))
        

            count = count+1
            print(count)
            time.sleep(5)
            today = datetime.now()
            iso_date = today.isoformat()
            client_socket.send(bytes(iso_date, "utf-8"))
            if count == 10:
                client_socket.close()
                
'''

'''
while True:
    # get current datetime
    today = datetime.now()
    # Get current ISO 8601 datetime in string format (YYYY-MM-DDTHH:MM:SS.mmmmmm)
    iso_date = today.isoformat()
    #print('ISO DateTime:', iso_date)

    print("server waiting for connection")
    client_socket, address = socket_server.accept() #it connects with the client 
    print(f"Connection from {address} has been established!")
    #clinentsocket.send(bytes(iso_date, "utf-8"))

    while True:
        #receiving data from client
        data = client_socket.recv(1024)
        if not data or data.decode("utf-8")=='END':
            break
        print("received from client client: %s "%data.decode("utf-8"))
        

        count = count+1
        print(count)
        time.sleep(5)
        today = datetime.now()
        iso_date = today.isoformat()
        client_socket.send(bytes(iso_date, "utf-8"))
        if count == 10:
            client_socket.close()
  
socket_server.close()
'''

            