numbers = input().split(' ')
numbers = list(map(int, numbers))
sum_numbers = 0
final_list = []

for num in range(len(numbers)):
    sum_numbers += numbers[num]

average_number = sum_numbers / len(numbers)

for i in range(len(numbers)):
    if numbers[i] > average_number:
        final_list.append(numbers[i])

if len(numbers) == 1 or not final_list:
    print("No")
else:
    final_list = list(reversed(sorted(final_list)))[:5]
    output = list(map(str, final_list))
    output = ' '.join(output)
    print(output)
