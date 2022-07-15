n = int(input())
word = input()
strings = list()

for i in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)

for current_string in strings:
    if word not in current_string:
        strings.remove(current_string)
print(strings)