from socket import *
serverPort = 6769
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#the paramaeter of listen is called "backlog" and
#it specifies the number of unaccepted connections that the system will allow
#before refusing new connections. If not specified, a default reasonable
#value is chosen.
    
def processString(s):
    operation = s[0]
    num1 = ''
    num2 = ''
    i = 2
    if s == "BYE":
        return "BYE"
    if operation == '-' or operation == '+' or operation == '*' or operation == '/':
        if s[1] != ' ':
            return "Invalid input"
        while i < len(s) and s[i] != ' ':
            num1 = num1 + s[i]
            i = i + 1
        if i == len(s):
            return "Invalid input"
        i = i + 1
        while i < len(s) and s[i] != ' ':
            num2 = num2 + s[i]
            i = i + 1
        equation = [operation, num1, num2]
        return equation
    else:
        return "Invalid input"

def performOperation(e):
    num1 = int(e[1])
    num2 = int(e[2])
    if e[0] == '+':
        return num1 + num2
    elif e[0] == '-':
        return num1 - num2
    elif e[0] == '*':
        return num1 * num2
    else:
        return num1 / num2
    
def main():
    print ('The server is ready to receive')
    busy = True
    while busy:
         connectionSocket, addr = serverSocket.accept()     
         userAction = connectionSocket.recv(1024).decode()
         #userAction = input("Please enter equation: ")
         userAction = processString(userAction)
         
         if userAction == "BYE":
             busy = False
         
         if userAction == "BYE" or userAction == "Invalid input":
             connectionSocket.send(userAction. encode())
             print(userAction)
         else:
        
             ans = performOperation(userAction)
             message = "The result of {num1} {operation} {num2} = {ans}".format(num1 = userAction[1], operation = userAction[0], num2 = userAction[2],ans = ans)
             connectionSocket.send(message. encode())
             print(message)
             
         connectionSocket.close()

main()
