text = input()
digits = ''
letters = ''
symbols = ''

for ch in text:
    if ch.isalnum():
        if ch.isdigit():
            digits += ch
        else:
            letters += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)
