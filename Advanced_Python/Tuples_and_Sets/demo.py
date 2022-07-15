tt = (1, 2, 3, 4, 2, 4, 3, 2, 5, 1, )
tt2 = ('1', '2', '3')

print(tt)
print(' --- count --- ')
print(tt.count(1))
print(tt.count(2))
print(tt.count(3))

print(' --- index --- ')
print(tt.index(1))
print(tt.index(1, 1))
print(tt.index(1, 7))

print(' --- in --- ')
print(1 in tt)
print(17 in tt)

print(' --- loops --- ')
for value in tt:
    print(value, end=' ')

print(' --- list comprehensions --- ')
[print(x, end=' ') for x in tt]

print(' --- other objects --- ')
print(f"str.join(): {', '.join(tt2)}")
print(f"len(): {len(tt)}")

print(' --- tuple concatenation --- ')
print((1,2) + (3, 4, 5))

print(' --- unpacking --- ')
tt = (1, 2, 3)
x, y, z = tt
# x, y, z = (1, 2, 3)