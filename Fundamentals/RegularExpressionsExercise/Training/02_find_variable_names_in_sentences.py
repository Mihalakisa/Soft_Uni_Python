import re

text = input()
regex = r"\b[_]([a-z]+)?([0-9]+)?([A-Z]{1})?([a-z]+)?\b"
disallowed_character = '_'

matches = re.finditer(regex, text)

output = list()

for match in matches:
    output.append(match.group())

output = ','.join(output)

for char in disallowed_character:
    output = output.replace(char, '')
print(output)
