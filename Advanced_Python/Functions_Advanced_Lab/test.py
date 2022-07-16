# def sum_nums(a, b=5):
#     return a + b
#
#
# print(sum_nums(5, 10))
# print(sum_nums(5))

def sum_nums(*args):
    result = 0
    for el in args:
        result += el
    return result
    # return sum(args)


print(sum_nums(10, -2, 3, 4, 15))
