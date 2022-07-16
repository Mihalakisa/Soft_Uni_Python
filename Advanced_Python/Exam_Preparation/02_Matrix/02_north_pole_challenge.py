def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def reposition_santa(row, col, rows, cols):
    if row < 0:
        return rows - 1, col
    if row >= rows:
        return 0, col
    if col < 0:
        return row, cols - 1
    if col >= cols:
        return row, 0


rows, cols = [int(x) for x in input().split(', ')]

matrix = []

player_row, player_col = 0, 0
decorations, decorations_collected = 0, 0
gifts, gifts_collected = 0, 0
cookies, cookies_collected = 0, 0

for row in range(rows):
    row_elements = input().split()
    for col in range(cols):
        if row_elements[col] == 'Y':
            player_row = row
            player_col = col
        elif row_elements[col] == 'D':
            decorations += 1
        elif row_elements[col] == 'G':
            gifts += 1
        elif row_elements[col] == 'C':
            cookies += 1

    matrix.append(row_elements)

end_condition = False

while True:
    if end_condition:
        print("Merry Christmas!")
        break

    line = input()
    if line == 'End':
        break
    data = line.split('-')
    command = data[0]
    steps = int(data[1])

    while steps and not end_condition:
        matrix[player_row][player_col] = 'x'
        player_row, player_col = get_next_pos(player_row, player_col, command)
        steps -= 1

        if is_outside(player_row, player_col, rows, cols):
            player_row, player_col = reposition_santa(player_row, player_col, rows, cols)

        if matrix[player_row][player_col] == 'D':
            decorations_collected += 1
            matrix[player_row][player_col] = 'x'
        elif matrix[player_row][player_col] == 'G':
            gifts_collected += 1
            matrix[player_row][player_col] = 'x'
        elif matrix[player_row][player_col] == 'C':
            cookies_collected += 1
            matrix[player_row][player_col] = 'x'

        matrix[player_row][player_col] = 'Y'
        if decorations == decorations_collected and gifts == gifts_collected and cookies == cookies_collected:
            end_condition = True


print("You've collected:")
print(f"- {decorations_collected} Christmas decorations")
print(f"- {gifts_collected} Gifts")
print(f"- {cookies_collected} Cookies")

for row in matrix:
    print(*row, sep=' ')
