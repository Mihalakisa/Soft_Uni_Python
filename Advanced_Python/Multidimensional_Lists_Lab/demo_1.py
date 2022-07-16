matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index], end='')
#     print()

for row_index in range(len(matrix)):
    print(*matrix[row_index])