n = int(input())
positive_nums = []
negative_nums = []
count_positive = 0
sum_negative = 0

for i in range(n):
    current_num = int(input())

    if current_num >= 0:
        count_positive += 1
        positive_nums.append(current_num)
    else:
        sum_negative += current_num
        negative_nums.append(current_num)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")
