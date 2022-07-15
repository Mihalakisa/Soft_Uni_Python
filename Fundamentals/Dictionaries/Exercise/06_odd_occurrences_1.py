words = input().split(' ')
words = list(map(lambda w: w.lower(), words))
occurrences = dict()

for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

for word in occurrences:
    if occurrences[word] % 2 != 0:
        print(word, end=' ')