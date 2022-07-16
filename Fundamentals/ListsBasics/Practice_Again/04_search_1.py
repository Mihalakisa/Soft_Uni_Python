n = int(input())
key_word = input()
all_list = []
filtered_list = []

for i in range(n):
    current_string = input()
    all_list.append(current_string)
    if key_word in current_string:
        filtered_list.append(current_string)

print(all_list)
print(filtered_list)
