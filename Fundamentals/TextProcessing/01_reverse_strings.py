text = input()

while text != 'end':
    rev = reversed(text)
    reversed_text = ''.join(rev)
    print(f"{text} = {reversed_text}")
    # reversed_text = ''
    # for char in rev:
    #     reversed_text += char

    text = input()
