n = int(input())
matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal = 0
for index in range(n):
    diagonal += matrix[index][index]
# for row_index in range(n):
#     for col_index in range(n):
#         if row_index == col_index:
#             diagonal += matrix[row_index][col_index]

print(diagonal)