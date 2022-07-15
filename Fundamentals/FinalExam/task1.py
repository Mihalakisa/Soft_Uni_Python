message = input()
result = 0

while True:
    info = input()
    if info == 'Finish':
        break

    data = info.split(' ')
    command = data[0]

    if command == 'Replace':
        current_char = data[1]
        new_char = data[2]
        message = message.replace(current_char, new_char)
        print(message)

    elif command == 'Cut':
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index >= 0 and end_index < (len(message)):
            message = message[:start_index] + message[end_index + 1:]
            print(message)
        else:
            print("Invalid indices!")

    elif command == 'Make':
        upper_lower = data[1]
        if upper_lower == 'Upper':
            message = message.upper()
            print(message)
        elif upper_lower == 'Lower':
            message = message.lower()
            print(message)

    elif command == 'Check':
        string = data[1]
        if string in message:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif command == 'Sum':
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index >= 0 and end_index < (len(message)):
            message_sum = message[start_index:end_index + 1]
            for i in message_sum:
                result += int(ord(i))
            print(result)
        else:
            print("Invalid indices!")