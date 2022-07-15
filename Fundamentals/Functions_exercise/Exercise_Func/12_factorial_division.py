def factorial(num):
    result_multi = 1
    for i in range(1, num + 1):
        result_multi *= i
    return result_multi


num1 = int(input())
num2 = int(input())

result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")
