def hello():
    print("Hello")
    
def processGreeting(g):
    if g == "hello":
        hello()
    else:
        print("?")

def processString(s):
    operation = s[0]
    num1 = ''
    num2 = ''
    i = 2
    while i < len(s) and s[i] != ' ':
        num1 = num1 + s[i]
        i = i + 1
    i = i + 1
    while i < len(s) and s[i] != ' ':
        num2 = num2 + s[i]
        i = i + 1
    equation = [operation, num1, num2]
    return equation

def performOperation(s):
    e = processString(s)
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
    equation = input("please input equation: ")
    ans = performOperation(equation)
    print(ans)
    
main()