import socket
s= socket.socket()
host = input(str("Please enter the host address of sender:"))
port =8080
s.connect((host, port))
print("connected...")

#recieve
f=open("/home/pi/Desktop/Soil Moisture Sensor/output.csv", "a") 
file_data =s.recv(1024)
f.write(file_data)
f.close() #to finish it off
print("File has been received successfully")