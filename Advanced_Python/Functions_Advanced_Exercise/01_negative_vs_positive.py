def find_positive_and_negative_sum(*args):
    positive_sum = 0
    negative_sum = 0

    for el in args:
        if el > 0:
            positive_sum += el
        else:
            negative_sum += el

    return positive_sum, negative_sum


nums = [int(x) for x in input().split()]


positive_sum, negative_sum = find_positive_and_negative_sum(*nums)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")