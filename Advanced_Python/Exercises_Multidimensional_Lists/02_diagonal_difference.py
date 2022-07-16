size = int(input())
matrix = []

for _ in range(size):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

primary = []
secondary = []
for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))