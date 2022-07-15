import re

output = list()
regex = r"\d+"
text = input()

while text != '':

    numbers = re.finditer(regex, text)
    for num in numbers:
        output.append(num.group())

    text = input()

print(' '.join(output))
