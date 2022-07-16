import re

number = int(input())
disallowed_character = '![]'

pattern = r'![A-Z][a-z]{2,}!:\[[a-zA-Z]{8,}\]'
command_pattern = r'![A-Z][a-z]{2,}!'
word_pattern = r'\[[a-zA-Z]{8,}\]'

for i in range(number):
    text = input()

    regex_result = re.finditer(pattern, text)
    regex_list = list()

    for regex in regex_result:
        regex_list.append(regex.group())

    if len(regex_list) > 0:
        command_reg = re.finditer(command_pattern, text)
        command_list = list()
        for word in command_reg:
            command_list.append(word.group())
        command = ''.join(command_list)

        text_reg = re.finditer(word_pattern, text)
        text_list = list()
        for word in text_reg:
            text_list.append(word.group())
        text = ''.join(text_list)

        for char in disallowed_character:
            command = command.replace(char, '')
        for char in disallowed_character:
            text = text.replace(char, '')

        print(f"{command}: ", end='')
        for letter in text:
            print(f"{ord(letter)}", end=' ')

    else:
        print("The message is invalid")