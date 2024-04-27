from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#the paramaeter of listen is called "backlog" and
#it specifies the number of unaccepted connections that the system will allow
#before refusing new connections. If not specified, a default reasonable
#value is chosen. 


print ('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()     
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence. encode())     
     connectionSocket.close()
