i = ['one', 'two', 'three', 'four', 'five', 'six']
print(i)
a, b = i.index('two'), i.index('three')
i[b], i[a] = i[a], i[b]
print(i)
# смяна на местата на 'two' и 'three' по индекс
