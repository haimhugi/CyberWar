import sys
import socket
import _thread
import time

SERVER_HOST1 = "192.168.10.5"
SERVER_HOST2 = "192.168.10.7"
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
gotResult = 0

# Define a function for the thread
def createTcpServer(threadName, port):
    global gotResult
    try: 
        success = 0
        s = socket.socket()
        #print("host:" + str(SERVER_HOST) + ", PORT:" + str(port))
        if threadName == 'Thread-1':
           #flag = 1
           s.bind((SERVER_HOST1, port))
        if threadName == 'Thread-2':
           #flag = 2
           s.bind((SERVER_HOST2, port+1))
        success = 1
    except Exception as e: 
        #print("failed to start server on port: " + str(port) + ", error: " + str(e))
        x=1
    if success == 1:
        s.listen(5)
        #if flag ==1:
         #print(f"Listening as {SERVER_HOST1}:{port} ...")
        #if flag == 2:
         #print(f"Listening as {SERVER_HOST2}:{port} ...")
        client_socket, client_address = s.accept()

        command = "1"
        client_socket.send(command.encode())
        output = client_socket.recv(BUFFER_SIZE).decode()
        # results, success = output.split(SEPARATOR)
        
        if 'result' in output and gotResult == 0:
            print(output)
            gotResult = 1


# Create two threads as follows
for port in range(1000, 4000, 40):
    try:
        _thread.start_new_thread( createTcpServer, ("Thread-1", port, ) )
        _thread.start_new_thread( createTcpServer, ("Thread-2", port, ) )
    except Exception as e:
        #print (e)
        x=1

while gotResult == 0:
    pass



