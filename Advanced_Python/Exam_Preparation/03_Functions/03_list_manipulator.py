def list_manipulator(numbers, command1, command2, *args):
    rotate_list = []
    pop_num = 0
    if command1 == 'add' and command2 == 'beginning':
        for i in range(len(args)):
            rotate_list.append(args[i])
        while rotate_list:
            pop_num = rotate_list.pop()
            numbers.insert(0, pop_num)

    elif command1 == 'add' and command2 == 'end':
        for i in range(len(args)):
            numbers.append(args[i])

    elif command1 == 'remove' and command2 == 'beginning':
        if args:
            for i in args:
                num = int(i)
                numbers = numbers[num:]
        else:
            numbers.pop(0)

    elif command1 == 'remove' and command2 == 'end':
        if args:
            num = args[0]
            for i in range(num):
                numbers.pop()
        else:
            numbers.pop()

    return numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
