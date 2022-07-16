days_of_tournament = int(input())
count_win = 0
count_lose = 0
money = 0
total_money = 0
sport = ''
day_win = 0
day_lose = 0

for i in range(1, days_of_tournament + 1):
    while True:
        sport = input()
        if sport == 'Finish':
            break
        condition = input()
        if condition == 'win':
            count_win += 1
            money += 20
        elif condition == 'lose':
            count_lose += 1
    if count_win > count_lose:
        money = money + (money * 0.1)
        day_win += 1

    elif count_win < count_lose:
        day_lose += 1

    total_money += money
    money = 0
    count_win = 0
    count_lose = 0

if day_win > day_lose:
    total_money = total_money + (total_money * 0.2)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
elif day_win < day_lose:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")