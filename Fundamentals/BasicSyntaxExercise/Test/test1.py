number = input()

sort_number = sorted(number, reverse=True)

for x, digit in enumerate(sort_number):
    print(digit, end="")