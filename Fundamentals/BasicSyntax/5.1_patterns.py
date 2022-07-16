number = int(input())

for i in range(number):
    print("*" * (i + 1))

for i in range(number-1, 0, -1):
    print("*" * i)