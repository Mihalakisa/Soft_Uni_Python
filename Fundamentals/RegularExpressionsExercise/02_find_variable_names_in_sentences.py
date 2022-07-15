import re

data = input()

patern = r'\b_[a-zA-Z0-9]+\b'

result = re.findall(patern, data)

words_list = []

for word in result:
    words_list.append(word[1:])

print(','.join(words_list))
