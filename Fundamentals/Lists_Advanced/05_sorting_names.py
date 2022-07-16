names = input().split(", ")

sorted_names = sorted(names)
sorted_names = sorted(sorted_names, key=lambda name: -len(name))

# whole_sorted_names = sorted(names, key=lambda name: (-len(name), name))

print(sorted_names)

# print(whole_sorted_names)
