password = input()
text = []

while True:
    info = input()
    if info == 'Done':
        break

    data = info.split()
    command = data[0]

    if command == 'TakeOdd':
        for i in range(len(password)):
            if i % 2 != 0:
                text.append(password[i])
        password = ''.join(text)
        print(password)

    elif command == 'Cut':
        index, length = int(data[1]), int(data[2])
        password = password[:index] + password[index+length:]
        print(password)

    elif command == 'Substitute':
        substring, substitute = data[1], data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
