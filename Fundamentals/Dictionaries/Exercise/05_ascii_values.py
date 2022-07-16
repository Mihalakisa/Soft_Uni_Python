text = input().split(', ')
dictionary = {char: ord(char) for char in text}

# -1-
# for char in text:
#     dictionary[char] = ord(char)

# -2-
# for i in range(len(text)):
#     key = text[i]
#     value = ord(text[i])
#     if key not in dictionary.keys():
#         dictionary[key] = int(value)

print(dictionary)
