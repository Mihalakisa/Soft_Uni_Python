import s
count = 0
word = ''
full_word = ''

while True:
    letter = input()


    if letter == 'End':
        print(word)
        break

    if letter == 'n' or letter == 'o' or letter == 'c':
        count += 1
        full_word += letter

        if count > 1:
            word += letter
            count = 0

        if full_word == 'n' and 'o' and 'c':
            word += " "
            full_word = 0
        continue

    word += letter
    count = 0