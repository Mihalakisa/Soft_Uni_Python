vowels = ["a", "o", "u", "e", "i"]
text = input()
no_vowels_text = [ch for ch in text if ch not in vowels]

# for ch in text:
#     if ch not in vowels:
#         no_vowels_text.append(ch)

print("".join(no_vowels_text))