import re

text = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)
# скобите са група а /1 е групата която ползваме или позицията на самата група

output = list()

for match in matches:
    output.append(match.group())

print(', '.join(output))
