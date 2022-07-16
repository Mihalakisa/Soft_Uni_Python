a, b = int(input()), int(input())

print(f"Before:")
print(f"a = {a}")
print(f"b = {b}")
a, b = b, a
print(f"After:")
print(f"a = {a}")
print(f"b = {b}")