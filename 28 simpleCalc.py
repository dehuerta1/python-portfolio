#David Huerta
#11/18/24


#Init

#Functions
#Adds two numbers and prints result
def add(num1, num2):
    result = num1 + num2
    print(result)

def sub(num1, num2):
    result = num1 - num2
    print(result)

def mult(num1, num2):
    result = num1 * num2
    print(result)

def div(num1, num2):
    result = num1 / num2
    print(result)

def simpleCalc():
    print("Welcome to Simple Calculator")
while True:
    print("Please choose an operation")
    print("""1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Quit""")

    option = int(input("1-5: "))
    if option == 1:
        num1 = int(input("please enter the first number"))
        num2 = int(input("please enter the second number"))
        print(add(num1,num2))

    if option == 2:
        num1 = int(input("please enter the first number"))
        num2 = int(input("please enter the second number"))
        print(sub(num1,num2))

    if option == 3:
        num1 = int(input("please enter the first number"))
        num2 = int(input("please enter the second number"))
        print(mult(num1,num2))

    if option == 4:
        num1 = int(input("please enter the first number"))
        num2 = int(input("please enter the second number"))
        print(div(num1,num2))

    if option == 5:
        print("bye")
        break

#Main
simpleCalc()
