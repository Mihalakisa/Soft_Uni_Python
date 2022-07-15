def absolute_value(nums):
    abs_list = []
    for n in nums:
        current_abs = abs(float(n))
        abs_list.append(current_abs)
    return abs_list


current_numbers = input().split(' ')
print(absolute_value(current_numbers))
