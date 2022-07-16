# t = (1, 2, 3)
t = ('apple', 'chery', 'banana')
# превръщаме в лист за да исменим стойността
y = list(t)
y[0] = 'orange'

print(tuple(y))