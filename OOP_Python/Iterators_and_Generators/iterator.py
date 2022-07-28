my_list = [4, 7, 0, 3]
# get an iterator using iter()
my_iter = iter(my_list)
print(next(my_iter))       # 4
print(next(my_iter))       # 7
print(my_iter.__next__())  # 0
print(my_iter.__next__())  # 3
next(my_iter)              # Error
