string_input = input()
result_string = ''
last_letter = ''

for letter in range(len(string_input)):
    if string_input[letter] != last_letter:
        result_string += string_input[letter]
        last_letter = string_input[letter]

print(result_string)
