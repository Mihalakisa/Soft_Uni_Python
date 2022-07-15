n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

key_word = input()

if key_word == "even":
    print(even)
elif key_word == "odd":
    print(odd)
elif key_word == "positive":
    print(positive)
elif key_word == "negative":
    print(negative)
