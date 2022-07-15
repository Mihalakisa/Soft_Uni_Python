word = input()
count = 0

while True:

    if count > 5:
        print("You need extra sleep")
        break
    if word == 'END':
        print(count)
        break

    if word == 'dog' or word == 'cat' or word == 'coding' or word == 'movie':
        count += 1
    if word == 'DOG' or word == 'CAT' or word == 'CODING' or word == 'MOVIE':
        count += 2

    word = input()