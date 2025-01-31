# Simple calculator app

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

playAgain = True


print("Welcome to the Simple Calculator App!")
while playAgain:
    print("Enter two numbers and an operator (+, -, *, /) to perform calculations")

    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))


    if op == "+":
        print("The result is: ", add(num1, num2))
    elif op == "-":
        print("The result is: ", subtract(num1, num2))
    elif op == "*":
        print("The result is: ", multiply(num1, num2))
    elif op == "/":
        print("The result is: ", divide(num1, num2))
    else:
        print("Invalid operator")

    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice == "y":
        playAgain = True
    else:
        playAgain = False
        print("Thank you for using the Simple Calculator App!")