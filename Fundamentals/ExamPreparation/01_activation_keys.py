text = input()

while True:
    current_text = input()

    if current_text == 'Generate':
        print(f"Your activation key is: {text}")
        break

    data = current_text.split('>>>')
    command = data[0]

    if command == 'Contains':
        substring = data[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif command == 'Flip':
        action = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        if action == 'Upper':
            text = text[:start_index] + text[start_index:end_index].upper() + text[end_index:]
            print(text)

        elif action == 'Lower':
            text = text[:start_index] + text[start_index:end_index].lower() + text[end_index:]
            print(text)

    elif command == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        text = text[0:start_index:] + text[end_index::]
        print(text)