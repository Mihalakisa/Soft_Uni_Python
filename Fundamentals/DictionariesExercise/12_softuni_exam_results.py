result_dict = {}
count_language = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    data = command.split('-')
    username = data[0]
    language = data[1]

    if language not in count_language and language != 'banned':
        count_language[language] = 1
    elif language in count_language and language != 'banned':
        count_language[language] += 1

    if language == 'banned':
        del result_dict[username]
        continue

    if username not in result_dict:
        score = int(data[2])
        result_dict[username] = score
    else:
        score = int(data[2])
        if int(result_dict[username]) < score:
            result_dict[username] = score

print("Results:")
for result in result_dict:
    print(f"{result} | {result_dict[result]}")
print("Submissions:")
for sub in count_language:
    print(f"{sub} - {count_language[sub]}")
