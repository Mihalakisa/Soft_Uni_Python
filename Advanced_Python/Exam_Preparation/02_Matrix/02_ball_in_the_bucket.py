def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 6
matrix = []

for _ in range(size):
    matrix.append(input().split())

hit_bucket = []
points = 0

for _ in range(3):

    data = input().replace('(', '').replace(')', '').split(', ')
    throw_row, throw_col = int(data[0]), int(data[1])

    if is_inside(throw_row, throw_col, size):
        if [throw_row, throw_col] in hit_bucket:
            continue
        if matrix[throw_row][throw_col] == 'B':
            if (throw_row, throw_col) not in hit_bucket:
                hit_bucket.append([throw_row, throw_col])
            for col_index in range(size):
                for row_index in range(size):
                    if col_index == throw_col:
                        if matrix[row_index][col_index].isdigit():
                            points += int(matrix[row_index][col_index])

diff = 0
if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    diff = 100 - points
    print(f"Sorry! You need {abs(diff)} points more to win a prize.")
