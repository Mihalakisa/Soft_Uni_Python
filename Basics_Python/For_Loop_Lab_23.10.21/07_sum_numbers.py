n = int(input())
# броят на числата
# за всяко число от първото до n-тото
# начало : 1
# край: n
# промяна: +1
# повтарям: прочитам (въвеждам) стойността и след това я сумирам
sum = 0
# сумата от числата

for number in range(1, n + 1):
    value = int(input())
    sum += value

print(sum)