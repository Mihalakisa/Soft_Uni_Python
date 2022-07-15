share = input().split(', ')
beggars = int(input())
outcome = []
counter = 0
begged_money = 0

while counter < beggars:

    for money in range(counter, int(len(share)), beggars):
        begged_money += int(share[money])

    outcome.append(begged_money)
    begged_money = 0
    counter += 1

print(outcome)