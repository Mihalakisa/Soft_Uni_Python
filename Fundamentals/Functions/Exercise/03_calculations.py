def calculations(operation, a, b):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return int(a / b)
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b


current_operation = input()
num1 = int(input())
num2 = int(input())
print(calculations(current_operation, num1, num2))
