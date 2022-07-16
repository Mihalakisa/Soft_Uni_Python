number = int(input())

positive = []
negative = []
sum_neg = 0

for i in range(number):
    current_number = int(input())

    if current_number >= 0:
        positive.append(current_number)

    else:
        negative.append(current_number)
        sum_neg += current_number

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum_neg}")
