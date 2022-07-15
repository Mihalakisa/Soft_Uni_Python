import re

count_barcode = int(input())
banned_symbols = '@#'
word_list = []
valid = False

pattern = r'((@)(#{1,}))[A-Z][a-zA-Z0-9]{4,}[A-Z]((@)(#{1,}))'
# word_pattern = r'[^\w]'

for i in range(count_barcode):
    text = input()
    regex = re.finditer(pattern, text)

    for word in regex:
        word_list.append(word.group())
        valid = True

    if valid:
        word = ''.join(word_list)
        # word = re.sub(r'[^\w]', '', word)
        regex_num = re.sub(r'[^\d]', '', word)

        if regex_num:
            print(f"Product group: {regex_num}")
        else:
            print("Product group: 00")

        word_list.clear()
        valid = False
    else:
        print("Invalid barcode")
