def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)

# If a function contains at least one < yield > statement,
# it becomes a < generator > function.
# Both yield and return will return a value from a function
# difference -> return - terminates a function entirely
# yield - pauses the function saving all its states and later continue from there


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed last')
    yield n


for num in my_gen():
    print(f"Outside generator n = {num}")