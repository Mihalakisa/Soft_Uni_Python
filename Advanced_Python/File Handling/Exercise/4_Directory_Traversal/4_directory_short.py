from os import walk

result = {}
for _, _, files in walk('.'):
    for file in files:
        ext = file.split('.')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(file)

for key, value in result.items():
    print(key, value)