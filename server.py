import socket
s= socket.socket()
host = input(str("Please enter the host address of sender:"))
port =8080
s.connect((host, port))
print("connected...")

#recieve
filename = input(str("please enter a filename for the incoming file: "))
file = open(filename, 'wb') # open in write byte mode
file_data =s.recv(1024)
file.write(file_data)
file.close() #to finish it off
print("File has been received successfully")