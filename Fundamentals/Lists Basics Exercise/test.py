gifts = input().split()
command = input().split()

while True:
    if "Money" in command:
        break

    elif command[0] == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == command[1]:
                gifts[index] = "None"

    elif command[0] == "Required":
        gifts_index = int(command[2])
        if 0 <= gifts_index < len(gifts):
            gifts[gifts_index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split()
    continue


for index in gifts:
    if index != "None":
        print(index, end=" ")
