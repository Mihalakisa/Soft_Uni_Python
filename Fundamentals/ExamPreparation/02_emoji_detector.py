import re

text = input()
cool_number = 1
disallowed_character = ':*'

emoji_pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})(\1)'
numbers = r'\d'

cool_count = re.findall(numbers, text)

for count in cool_count:
    cool_number *= int(count)

emoji_result = re.finditer(emoji_pattern, text)
emoji_list = list()

for emoji in emoji_result:
    emoji_list.append(emoji.group())

sum_letters = 0
final_emoji_result = list()

for word in emoji_list:
    for letter in word:
        if letter.isalpha():
            sum_letters += ord(letter)
    if sum_letters >= cool_number:
        final_emoji_result.append(word)
    sum_letters = 0

print(f"Cool threshold: {cool_number}")
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emoji in final_emoji_result:
    print(emoji)