import re

text = input()
cool_number = 1
disallowed_character = ':*'

emoji_pattern = r'([:|*]{2})[A-Z][a-z]{2,}\1'
numbers = r'\d'
words_emoji = r'\w+'

cool_count = re.finditer(numbers, text)

for count in cool_count:
    cool_number *= int(count.group())

emoji_result = re.finditer(emoji_pattern, text)
emoji_list = list()

for emoji in emoji_result:
    emoji_list.append(emoji.group())
emoji_list = ', '.join(emoji_list)

simple_words = re.finditer(words_emoji, emoji_list)
words_list = list()

for word in simple_words:
    words_list.append(word.group())
print(words_list)