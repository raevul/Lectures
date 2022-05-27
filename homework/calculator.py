num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num = input("Select operation: +, -, *, /, **, //, %: ")

if num == '+':
    print("Addition result: ", num1 + num2)
elif num == '-':
    print("Subtraction result: ", num1 - num2)
elif num == '*':
    print("Multiplication result: ", num1 * num2)
elif num == '/':
    print("Division result: ", num1 / num2)
elif num == '**':
    print("Result of exponentiation: ", num1 ** num2)
elif num == '//':
    print("Result remainder of division: ", num1 // num2)
elif num == '%':
    print("Result of integer division: ", num1 % num2)
else:
    print("This operation is not in the system!")









