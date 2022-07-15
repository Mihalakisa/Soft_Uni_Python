numbers = input().split(' ')
turns_count = 0
middle = ''

line = input()

while line != 'end':
    index_list = line.split(' ')
    index1 = int(index_list[0])
    index2 = int(index_list[1])
    turns_count += 1
    add_text = f'-{turns_count}a'

    if 0 <= index1 < len(numbers) and 0 <= index2 < len(numbers) and index1 != index2:
        if numbers[index1] == numbers[index2]:
            save_index = numbers[index1]
            numbers.pop(index1)
            if index1 > index2:
                numbers.pop(index2)
            elif index1 < index2:
                numbers.pop(index2 - 1)
            print(f"Congrats! You have found matching elements - {save_index}!")

        else:
            print("Try again!")
    else:
        middle = round(len(numbers) / 2)
        numbers.insert(int(middle), add_text)
        numbers.insert(int(middle), add_text)
        print("Invalid input! Adding additional elements to the board")

    if len(numbers) == 0 or len(numbers) == 1:
        break

    line = input()

numbers = list(map(str, numbers))
output = ' '.join(numbers)

if len(numbers) > 1:
    print("Sorry you lose :(")
    print(output)
else:
    print(f"You have won in {turns_count} turns!")
