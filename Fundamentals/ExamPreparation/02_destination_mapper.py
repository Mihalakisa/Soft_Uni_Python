import re

regex = r"([/=])?([A-Z][A-Za-z]{2,})\1"
disallowed_character = '/='

text = input()

matches = re.finditer(regex, text)

output = list()

for match in matches:
    output.append(match.group())

output = ', '.join(output)

for char in disallowed_character:
    output = output.replace(char, '')

print(f"Destinations: {output}")

output = output.split(', ')
travel_points = 0
for word in output:
    travel_points += int(len(word))
print(f"Travel Points: {travel_points}")
