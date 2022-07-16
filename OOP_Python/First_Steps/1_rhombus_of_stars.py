def get_line(i, n):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + '* ' * stars_count


def print_line(n):
    print(get_line(n - 1, n - 1))


def print_square(n):
    [print(get_line(n - 1, n - 1)) for _ in range(n)]


def print_rhombus(n):
    # [print(get_line(i, n)) for i in range(n)]
    # [print(get_line(i, n)) for i in range(n - 2, -1, -1)]
    for i in range(n):
        print(get_line(i, n))
    for i in range(n - 2, -1, -1):
        print(get_line(i, n))


print_rhombus(int(input()))
print_line(4)
print_square(3)
