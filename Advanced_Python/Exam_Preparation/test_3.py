def next_move(command, row, col, rows, cols):
    if command == 'up':
        if row - 1 < 0:
            return rows - 1, col
        else:
            return row - 1, col
    if command == 'left':
        if col - 1 < 0:
            return row, cols - 1
        else:
            return row, col - 1
    if command == 'right':
        if col + 1 >= cols:
            return row, 0
        else:
            return row, col + 1
    if command == 'down':
        if row + 1 >= rows:
            return 0, col
        else:
            return row + 1, col


rows, cols = [int(x) for x in input().split(', ')]
matrix = []
santa_row = 0
santa_col = 0
gifts = 0
cookies = 0
decorations = 0
collected_gifts = 0
collected_cookies = 0
collected_decorations = 0
merry_christmas = False
for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(cols):
        if matrix[row][col] == 'Y':
            santa_row = row
            santa_col = col
        elif matrix[row][col] == 'D':
            decorations += 1
        elif matrix[row][col] == 'G':
            gifts += 1
        elif matrix[row][col] == 'C':
            cookies += 1

while True:
    if merry_christmas:
        break
    command = input()
    if command == 'End':
        break
    commands = command.split('-')
    direction = commands[0]
    steps = int(commands[1])

    while steps and not merry_christmas:
        next_row, next_col = next_move(direction, santa_row, santa_col, rows, cols)
        steps -= 1
        if matrix[next_row][next_col] == 'D':
            decorations -= 1
            collected_decorations += 1
        elif matrix[next_row][next_col] == 'C':
            cookies -= 1
            collected_cookies += 1
        elif matrix[next_row][next_col] == 'G':
            gifts -= 1
            collected_gifts += 1

        matrix[santa_row][santa_col] = 'x'
        santa_row, santa_col = next_row, next_col
        matrix[next_row][next_col] = 'Y'
        if not gifts:
            if not cookies:
                if not decorations:
                    merry_christmas = True

if merry_christmas:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")
for row in matrix:
    print(*row)