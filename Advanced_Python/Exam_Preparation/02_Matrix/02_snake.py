def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = []
count = 1
food, eaten_food = 0, 0
snake_row, snake_col = 0, 0
b_one_row, b_one_col = 0, 0
b_two_row, b_two_col = 0, 0
lose_condition = False

for row in range(size):
    data = [x for x in input()]
    row_elements = data
    for col in range(size):
        if row_elements[col] == 'S':
            snake_row = row
            snake_col = col
        elif row_elements[col] == 'B':
            if count == 1:
                b_one_row = row
                b_one_col = col
                count += 1
            else:
                b_two_row = row
                b_two_col = col
        elif row_elements[col] == '*':
            food += 1

    matrix.append(row_elements)


while True:
    command = input()
    current_row, current_col = get_next_pos(snake_row, snake_col, command)

    if not is_inside(current_row, current_col, size):
        matrix[snake_row][snake_col] = '.'
        lose_condition = True
        break
    else:
        matrix[snake_row][snake_col] = '.'
        if matrix[current_row][current_col] == '*':
            eaten_food += 1
        elif matrix[current_row][current_col] == 'B':
            matrix[current_row][current_col] = '.'
            if current_row == b_one_row and current_col == b_one_col:
                current_row, current_col = b_two_row, b_two_col
                matrix[current_row][current_col] = '.'
            elif current_row == b_two_row and current_col == b_two_col:
                current_row, current_col = b_one_row, b_one_col
                matrix[current_row][current_col] = '.'

    snake_row, snake_col = current_row, current_col
    matrix[snake_row][snake_col] = 'S'
    if eaten_food >= 10:
        break

if eaten_food < 10 or lose_condition:
    print("Game over!")
    print(f"Food eaten: {eaten_food}")
    for row in matrix:
        print(''.join(row))

if eaten_food >= 10 or not lose_condition:
    print("You won! You fed the snake.")
    print(f"Food eaten: {eaten_food}")
    for row in matrix:
        print(''.join(row))