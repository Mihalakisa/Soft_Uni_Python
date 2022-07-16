line = input()
is_done = False
final_str = ""
x = -1
while True:
    has_digits = False
    if x == len(line) - 1:
        break
    for ch in range(x + 1, len(line)):
        if line[ch].isdigit():
            has_digits = True
        if ch == len(line) - 1 and not has_digits:
            is_done = True
    if is_done:
        break
    current_word = ""
    current_digit = ""
    temp_end = False
    list_line = [z for z in line]
    digits_to_remove = []
    for x in range(x, len(list_line)):
        if not list_line[x].isdigit():
            if not temp_end:
                current_word += list_line[x].upper()
            else:
                break
        else:
            current_digit += list_line[x]
            temp_end = True
    current_digit = int(current_digit)
    final_str += current_word * current_digit
    line = "".join(list_line)
    last_character = x

print(f"Unique symbols used: {len(set(final_str))}")
print(final_str)
