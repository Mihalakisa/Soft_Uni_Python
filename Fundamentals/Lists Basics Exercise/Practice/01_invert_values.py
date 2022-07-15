numbers = input().split()
opposite_numbers = []

for x in range(len(numbers)):
    current_numbers = -int(numbers[x])
    opposite_numbers.append(current_numbers)
print(opposite_numbers)
