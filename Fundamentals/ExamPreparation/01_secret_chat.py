message = input()
new_message = ''

while True:
    info = input()

    if info == 'Reveal':
        print(f"You have a new text message: {message}")
        break

    data = info.split(':|:')
    command = data[0]
    index1 = data[1]

    if command == 'InsertSpace':
        message = message[:int(index1)] + ' ' + message[int(index1):]
        print(message)

    elif command == 'Reverse':
        if index1 in message:
            rev_index = index1[::-1]
            message = message.replace(index1, '', 1)
            message += rev_index
            print(message)
        else:
            print("error")

    elif command == 'ChangeAll':
        index2 = data[2]
        message = message.replace(index1, index2)
        # for i in message:
        #     if index1 in i:
        #         new_message += index2
        #     else:
        #         new_message += i
        # message = new_message
        print(message)
