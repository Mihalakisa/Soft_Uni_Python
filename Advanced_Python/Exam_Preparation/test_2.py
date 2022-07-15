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

player_row, player_col = 0, 0
decorations, decorations_collected = 0, 0
gifts, gifts_collected = 0, 0
cookies, cookies_collected = 0, 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    # row_elements = input().split()
    for col in range(cols):
        if matrix[row][col] == 'Y':
            player_row = row
            player_col = col
        elif matrix[row][col] == 'D':
            decorations += 1
        elif matrix[row][col] == 'G':
            gifts += 1
        elif matrix[row][col] == 'C':
            cookies += 1

    # matrix.append(row_elements)

merry_christmas = False

while True:
    if merry_christmas:
        print("Merry Christmas!")
        break

    line = input()
    if line == 'End':
        break
    data = line.split('-')
    command = data[0]
    steps = int(data[1])

    while steps and not merry_christmas:

        next_row, next_col = next_move(command, player_row, player_col, rows, cols)
        steps -= 1

        if matrix[next_row][next_col] == 'D':
            decorations_collected += 1
        elif matrix[next_row][next_col] == 'G':
            gifts_collected += 1
        elif matrix[next_row][next_col] == 'C':
            cookies_collected += 1

        matrix[player_row][player_col] = 'x'
        player_row, player_col = next_row, next_col
        matrix[next_row][next_col] = 'Y'

        if decorations == decorations_collected and gifts == gifts_collected and cookies == cookies_collected:
            merry_christmas = True

print("You've collected:")
print(f"- {decorations_collected} Christmas decorations")
print(f"- {gifts_collected} Gifts")
print(f"- {cookies_collected} Cookies")

for row in matrix:
    print(*row, sep=' ')
