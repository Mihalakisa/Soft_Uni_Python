import re

pattern = r'\d+'

while True:
    text = input()

    if not text:
        break

    result = re.findall(pattern, text)

    if len(result) > 0:
        print(' '.join(result), end=' ')