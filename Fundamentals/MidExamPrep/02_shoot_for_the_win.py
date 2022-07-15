targets = input().split(' ')
targets = list(map(int, targets))
current_number = 0
count_hit = 0
change_number = 0

while True:
    command = input()
    if command == 'End':
        targets = ' '.join(map(str, targets))
        print(f"Shot targets: {count_hit} -> {targets}")
        break

    target_index = int(command)

    for i in range(len(targets)):
        if i == target_index:
            current_number = targets[i]
            for y in range(len(targets)):
                change_number = targets[y]
                if targets[y] == -1:
                    continue
                if current_number < change_number:
                    targets[y] -= current_number
                elif current_number >= change_number:
                    targets[y] += current_number

            targets[i] = -1
            if targets[i] == -1:
                count_hit += 1
