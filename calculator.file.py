print("Calculator")

num1 = float(input("Enter your first number: "))
operation = input("Choose +, -, * or /: ")
num2 = float(input("Enter your second number: "))

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

else:
    print("Invalid operation")
