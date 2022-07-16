import re

text = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = re.finditer(regex, text)
output = list()

for match in matches:
    output.append(match.group())

print(' '.join(output))
