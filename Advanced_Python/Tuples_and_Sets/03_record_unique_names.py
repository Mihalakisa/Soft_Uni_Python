# n = int(input())
#
# name_set = set()
#
# for _ in range(n):
#     name_set.add(input())
#
# # [print(name) for name in name_set]
# for name in name_set:
#     print(name)

n = int(input())

names_set = {input() for _ in range(n)}
[print(name) for name in names_set]