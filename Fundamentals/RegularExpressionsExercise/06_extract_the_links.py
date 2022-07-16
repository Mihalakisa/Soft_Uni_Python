import re

pattern = r'www\.(([a-zA-Z[0-9?]+[-])*([a-zA-Z[0-9?]+)*)\.(([a-zA-Z]+(-)*)((\.)*([a-zA-Z0-9]+))*)'

sites_list = []

while True:
    text = input()

    if not text:
        break

    result = re.finditer(pattern, text)
    for txt in result:
        sites_list.append(txt.group())

print('\n'.join(sites_list))
