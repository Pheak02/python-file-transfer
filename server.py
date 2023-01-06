import socket #allow the connection
s=socket.socket() # initialize the socket object
host=socket.gethostname() #give the host address of the program, where the client.py will connect to
port =8080 #can set to anything we like
s.bind((host, port)) #bind socket to 8080
s.listen(1) # will listen to coming connection , listen to only 1 computer
print(host)
print("Waiting for any coming connection..")
conn, addr =s.accept()
print(addr,"Has connected to the server")

#create the file transfer
filename = input(str("Please enter the filename: "))
# Open it in read byte mode
file = open(filename, 'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")