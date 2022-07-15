secret_command = ["c", "o", "n"]
message = []
met_command = []
result = ""

while True:
    alphabet = input()

    if alphabet == "End":
        print(result)
        break
    if alphabet.isalpha():
        if alphabet in secret_command:
            if alphabet in met_command:
                message.append(alphabet)
            else:
                met_command.append(alphabet)
        else:
            message.append(alphabet)

        check = all(item in met_command for item in secret_command)
        if check is True:
            for a in message:
                result += str(a)
            result += " "
            met_command.clear()
            message.clear()