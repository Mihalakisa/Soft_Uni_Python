words = input().split(' ')
new_sentence = ''

for word in words:
    digit = ''
    first_part = ''
    second_part = []

    for i in word:
        if i.isdigit():
            digit += i

        else:
            second_part.append(i)

    if len(second_part) > 1:
        second_part[0], second_part[-1] = second_part[-1], second_part[0]

    first_part = chr(int(digit))

    for letter in second_part:
        first_part += letter

    new_sentence += first_part + ' '

print(new_sentence)
