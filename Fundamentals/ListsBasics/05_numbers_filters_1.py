number = int(input())

positive = list()
negative = list()
even = list()
odd = list()

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

filter_word = input()

print(eval(filter_word))

# if filter_word == 'even':
#     print(even)
# if filter_word == 'odd':
#     print(odd)
# if filter_word == 'positive':
#     print(positive)
# if filter_word == 'negative':
#     print(negative)
