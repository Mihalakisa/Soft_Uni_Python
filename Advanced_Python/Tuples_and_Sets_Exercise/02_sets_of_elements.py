n, m = [int(x) for x in input().split()]

first = set()
# [first.add(int(input())) for _ in range(n)]
second = set()
# [second.add(int(input())) for _ in range(n)]

for _ in range(n):
    first.add(input())

for _ in range(m):
    second.add(input())

result = first.intersection(second)

for num in result:
    print(num)