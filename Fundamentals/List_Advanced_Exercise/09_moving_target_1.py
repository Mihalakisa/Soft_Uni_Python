targets = input().split(' ')

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
            number = int(targets[position]) - power
            targets[position] = str(number)
            if number <= 0:
                targets.pop(position)

    elif action_command == 'Strike':
        indexStrike = position + power
        indexStrikeSecond = position - power
        if 0 <= indexStrike < len(targets) and 0 <= indexStrikeSecond < len(targets):
            targets.pop(indexStrike)
            targets.pop(indexStrikeSecond)
            targets.pop(position - 1)
        else:
            print("Strike missed!")

    elif action_command == 'Add':
        if 0 <= position < len(targets):
            targets.insert(position, str(power))
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
