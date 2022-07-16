message = input()

while True:
    text = input()

    if text == 'Decode':
        break

    data = text.split('|')
    command = data[0]
    position = data[1]

    if command == 'Move':
        for i in range(int(position)):
            message = message[1:]+message[0]

    elif command == 'Insert':
        letter = data[2]
        message = f"{message[:int(position)]}{letter}{message[int(position):]}"

    elif command == 'ChangeAll':
        letter = data[2]
        message = message.replace(position, letter)

print(f"The decrypted message is: {message}")