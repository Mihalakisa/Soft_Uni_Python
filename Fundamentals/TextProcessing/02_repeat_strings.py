words = input().split()
output = ''

for word in words:
    output += word * len(word)

print(output)
