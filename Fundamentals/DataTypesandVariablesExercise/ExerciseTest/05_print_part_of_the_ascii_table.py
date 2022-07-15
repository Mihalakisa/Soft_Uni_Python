start = int(input())
finish = int(input())
is_true = False

while not is_true:
    print(f"{chr(start)}", end=' ')

    is_true = start == finish

    start += 1