key = int(input())
lines = int(input())
message = ''

for i in range(lines):
    letter = input()
    message = ord(letter) + key
    print(chr(message), end='')