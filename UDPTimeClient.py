from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Type "date & time" to request the time and date from the server:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
date_time, serverAddress = clientSocket.recvfrom(2048)
print (date_time.decode())
clientSocket.close()
