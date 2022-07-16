targets = input().split(' ')
targets = list(map(int, targets))

while True:
    command = input()

    if command == 'End':
        break

    op_command = command.split(' ')
    action_command = op_command[0]
    position = int(op_command[1])
    power = int(op_command[2])

    if action_command == 'Shoot':
        if 0 <= position < len(targets):
            number = targets[position] - power
            targets[position] = number
            if number <= 0:
                targets.pop(position)

    elif action_command == 'Strike':
        position_strike = position + power
        position_strike_second = position - power
        if 0 <= position_strike < len(targets) and 0 <= position_strike_second < len(targets):
            targets.pop(position_strike)
            targets.pop(position_strike_second)
            targets.pop(position - 1)

        else:
            print("Strike missed!")

    elif action_command == 'Add':
        if 0 <= position < len(targets):
            targets.insert(position, power)
        else:
            print("Invalid placement!")

result = ''
ind = 1
for x in targets:
    if ind == 0 or ind == len(targets):
        result += str(x)
    else:
        result += str(x) + '|'
    ind += 1
print(result)
