# def check_even(nums):
#     if nums % 2 == 0:
#         return True
#
#     return False
#
#
# result = filter(check_even, list(map(int, input().split(' '))))
# print(list(result))

result = list(filter(lambda x: x % 2 == 0, map(int, input().split(' '))))
print(result)
