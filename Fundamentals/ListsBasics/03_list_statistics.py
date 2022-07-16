number = int(input())

negatives = list()
positives = list()
sum_of_negatives = 0

for i in range(number):
    current = int(input())
    if current >= 0:
        positives.append(current)
    else:
        negatives.append(current)
        sum_of_negatives += current

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum_of_negatives}")
