key_line = int(input())
numbers_line = int(input())
message = ''

for num in range(1, numbers_line + 1):
    letter = input()
    message = ord(letter) + key_line
    print(chr(message), end='')