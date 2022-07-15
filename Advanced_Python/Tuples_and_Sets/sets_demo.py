'''
Sets:

- Search, add, remove is very, very, very fast
- Contains only unique values
    - * unique values
- Unordered (with hash tables)
- Ordered (with tree)
'''

ss = {2, 3, 4, 5}
print(ss)
[ss.add(1) for _ in range(1024)]
print(ss)
sss = set()   # <-- this is set

# add
ss.add(8)
# remove
ss.remove(4)
# check if value is in set
print(4 in ss)
