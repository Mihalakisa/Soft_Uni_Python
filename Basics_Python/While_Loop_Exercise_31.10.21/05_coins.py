change_money = int(float(input()) * 100)
number_of_coins = 0

while change_money > 0:

    number_of_coins += 1

    if change_money >= 200:
        change_money -= 200

    elif change_money >= 100:
        change_money -= 100

    elif change_money >= 50:
        change_money -= 50

    elif change_money >= 20:
        change_money -= 20

    elif change_money >= 10:
        change_money -= 10

    elif change_money >= 5:
        change_money -= 5

    elif change_money >= 2:
        change_money -= 2

    elif change_money >= 1:
        change_money -= 1

print(number_of_coins)