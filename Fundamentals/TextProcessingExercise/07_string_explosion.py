text = input()
strength = 0
new_text = ''

for ch in range(len(text)):
    if text[ch] != '>':
        if strength > 0:
            strength -= 1
        else:
            new_text += text[ch]

    elif text[ch] == '>':
        new_text += text[ch]
        strength += int(text[ch + 1])

print(new_text)
