text = input()
upper_letters = []

for x in range(len(text)):
    if text[x].isupper():
        upper_letters.append(x)

print(upper_letters)