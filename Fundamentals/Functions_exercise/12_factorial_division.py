def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)

    # f = 1
    # if num >= 1:
    #     for i in range(1, num + 1):
    #         f = f * i
    # return f


numb1 = int(input())
numb2 = int(input())
result = factorial(numb1) / factorial(numb2)
print(f"{result:.2f}")
