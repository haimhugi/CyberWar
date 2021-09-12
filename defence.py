import socket
import os
import subprocess
import sys
import socket
import _thread

SERVER_HOST = "192.168.10.20"
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

# Define a function for the thread
def connectTcpServer(threadName, port):
    try:
        #print("port" + str(port))
        s = socket.socket()
        s.connect((SERVER_HOST, port))
        # receive the command from the server
        print("we connect to yakov server with port" + str(port))
        command = s.recv(BUFFER_SIZE).decode()
        message = "Haha we blocked your attack , mabey next time (:"
        s.send(message.encode())
      
    except Exception as e:
        #print("not connected" +str(port))
        x=1


# Create two threads as follows
while 1:
  try:
      port1 = 22
      port2 = 5555
      _thread.start_new_thread( connectTcpServer, ("thread-1", port1, ) )
      _thread.start_new_thread( connectTcpServer, ("thread-2", port2, ) )
  except Exception as e:
      print (e)
  pass

while 1:
    pass
