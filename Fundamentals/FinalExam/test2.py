import re

number = int(input())
disallowed_character = '![]'
count = 1

pattern = r'([!])[A-Z][a-z]{2,}\1[:][\[][a-zA-Z]{8,}[\]]'

for i in range(number):
    text = input()

    regex_result = re.finditer(pattern, text)
    regex_list = list()

    for regex in regex_result:
        regex_list.append(regex.group())

    regex_list = ''.join(regex_list)

    if len(regex_list) > 0:
        for char in disallowed_character:
            regex_list = regex_list.replace(char, '')

        result = regex_list.split(':')
        command = result[0]
        word = result[1]

        print(f"{command}: ", end='')
        for letter in word:
            if count == len(word):
                print(f"{ord(letter)}")
            else:
                print(f"{ord(letter)}", end=' ')
                count += 1

    else:
        print("The message is invalid")
