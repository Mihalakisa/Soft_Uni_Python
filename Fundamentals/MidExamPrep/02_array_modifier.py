numbers = input().split(' ')

while True:
    command = input()

    if command == 'end':
        print(', '.join(numbers))
        break

    if command == 'decrease':
        for i in range(len(numbers)):
            number = numbers[i]
            number = int(number) - 1
            numbers[i] = str(number)
        continue

    operation = command.split(' ')
    command_operation = operation[0]
    first_index = int(operation[1])
    second_index = int(operation[2])

    if command_operation == 'swap':
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

    elif command_operation == 'multiply':
        multiply_num = int(numbers[first_index]) * int(numbers[second_index])
        numbers[first_index] = str(multiply_num)
