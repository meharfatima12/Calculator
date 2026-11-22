# TODO: put the calculator in a while True loop so it repeats
#calculator
try:
    num1 = float(input("enter the first number: "))
    operation = input("enter an operation(+, -, *, /): ")
    num2 = float(input("enter the second number: "))
except ValueError:
    print("please enter digits only")
else:
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("cannot divide by zero")
    else:
        print("invalid operation")