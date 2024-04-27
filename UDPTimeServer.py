from socket import *
from time import gmtime, strftime
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    if request.decode() == "date & time":
        date_time = strftime("Date: %b %d, %Y. Time: %I:%M%p", gmtime())
    else:
        date_time = "invalid input"
    serverSocket.sendto(date_time.encode(), clientAddress)

