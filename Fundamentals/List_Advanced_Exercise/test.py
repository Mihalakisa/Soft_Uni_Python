# test = [num for num in range(1, 11) if num % 2 == 0]
# print(test)
# ^ List Comprehension ^

# test = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(f"Comprehension - {test}")
#
# combination = []
#
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combination.append((x, y))
#
# print(combination)

# test = list(map(int, input().split(', ')))  # тук са като числа
# test1 = input().split(', ')                 # тук са стрингове или текст
# print(test)
# print(test1)

# test = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# test = list(filter(lambda x: x % 2 == 0, map(int, input().split(' '))))
# print(test)

def filter_func(num):
    if num % 2 == 0:
        return True

    return False


test = list(filter(filter_func, map(int, input().split(' '))))
print(test)
