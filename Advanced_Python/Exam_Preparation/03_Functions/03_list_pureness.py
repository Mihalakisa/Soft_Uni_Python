import sys


def best_list_pureness(numbers, n):
    res = 0
    rotation = 0
    best_number = -sys.maxsize
    for i in range(0, n + 1):
        count = 0
        res = 0
        for num in numbers:
            res += num * count
            if res > best_number:
                best_number = res
                rotation = i
            count += 1
        numbers.insert(0, numbers.pop())

    return f"Best pureness {best_number} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
print()
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
print()
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)