size = int(input())
matrix = []

for _ in range(size):
    nums = [int(x) for x in input().split(', ')]
    matrix.append(nums)

primary = []
secondary = []
for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])
    # secondary.append(matrix[index][-1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
