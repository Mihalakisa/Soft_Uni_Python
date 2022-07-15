gifts = input().split()
command = input().split()

while True:
    if 'Money' in command:
        break

    elif command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        gifts_index = int(command[2])
        if 0 <= gifts_index < len(gifts):
            gifts[gifts_index] = command[1]

    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

    command = input().split()
    continue

for i in gifts:
    if i != 'None':
        print(i, end=' ')
