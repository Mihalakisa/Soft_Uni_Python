number = int(input())
even = []
odd = []
positive = []
negative = []

for i in range(number):
    current_number = int(input())

    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

command = input()

print(eval(command))