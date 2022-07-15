text = input()
letter = ''
result = ''

for ch in range(len(text)):
    if text[ch] != letter:
        letter = text[ch]
        result += letter

print(result)
