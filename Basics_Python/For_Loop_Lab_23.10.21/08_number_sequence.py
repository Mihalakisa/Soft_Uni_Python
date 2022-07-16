import sys

n = int(input())
#  за всяко число от първото до n-тото
# начало: 1 (първо число)
# край: n (последно число)
# промяната: =1
# повтарям: прочитам стойност от конзолата + проверка дали е максимално

max = -sys.maxsize
# моментен максимум
min = sys.maxsize
# моментен минимум
for number in range(1, n + 1):
    value = int(input())
    # проверка дали е макс
    if value > max:
        max = value
    if value < min:
        min = value

print(f"Max number: {max}")
print(f"Min number: {min}")