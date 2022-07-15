# test = ('arg1', 'arg2', 'arg3')
# val = [1, 2, 3]
# my_dict = dict.fromkeys(test, val)
#
# print(my_dict)

# data = ['one', 'two', 'three']
# numbers = [1, 2, 3]
# result = dict(zip(data, numbers))
#
# print(result)

# messed_dict = {'c': 3, 'b': 2, 'a': 1}
#
# for key, value in sorted(messed_dict.items()):
#     print(f"{key} - {value}")

# number = [1, 2, 3]
# square_dict = {x: x**2 for x in number}
#
# print(square_dict)

people = {1: {'name': 'Mike', 'age': 22}, 2: {'name': 'John', 'age': 33}}
print(people[2]['name'])
