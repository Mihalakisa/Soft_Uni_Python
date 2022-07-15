number = int(input())
key_word = input()

list_strings = []
filtered = []

for i in range(number):
    string = input()
    list_strings.append(string)
    if key_word in string:
        filtered.append(string)

print(list_strings)
print(filtered)
