def rounding(nums):
    nums_list = []
    for n in nums:
        result_round = round(float(n))
        nums_list.append(result_round)
    return nums_list


numbers = input().split(' ')
print(rounding(numbers))
