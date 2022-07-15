def characters_in_range(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')


start_string = input()
end_string = input()

characters_in_range(start_string, end_string)
