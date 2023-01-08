import math

print("Welcome to my calculator")

while True:
    print('~~~~~~~~~~~~~~~~~~')
    print("+ : sum")
    print("- : sub")
    print("* : mul")
    print("/ : div")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("sqrt")
    print("factorial")
    print("Exit")
    print('~~~~~~~~~~~~~~~~~~')

    op = input("please enter ypur choice: ")

    if op == 'Exit':
        print("Hope to meet!")
        break

    elif op == "+" or op == "-" or op == "*" or op =="/":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))

    elif op == "sin" or op == "cos" or op == "tan" or op == "cot":
        a = float(input("enter number: "))
        Degree = a * 180 / math.pi

    elif op == 'sqrt' or op == 'factorial':
        a = int(input('enter number: '))

    else:
        result = 'oprator not found!'
  

    if op == "+":
        result = a + b

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        if b == 0:
            result = "cannot divide by zero"
        else:
            result = a / b

    elif op == "sin":
        result = math.sin(Degree)

    elif op == "cos":
        result = math.cos(Degree)
    
    elif op == "tan":
        result == math.tan(Degree)

    elif op == "cot":
        result == math.cot(Degree)

    elif op == "sqrt":
        if a <= 0:
            print('enter 0 or hightr')
        else:
            result = math.sqrt(a)

    elif op == "factorial":
        result = math.factorial(a)

 
    print('result= ', result)



