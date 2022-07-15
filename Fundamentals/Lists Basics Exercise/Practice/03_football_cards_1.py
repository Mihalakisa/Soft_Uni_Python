team_a = 11
team_b = 11
number_red_cards = input().split(' ')
player_loses = []
condition = False

for card in number_red_cards:
    if card not in player_loses:
        player_loses.append(card)
        if 'A' in card:
            team_a -= 1
        elif 'B' in card:
            team_b -= 1
        if team_a < 7 or team_b < 7:
            condition = True
            break
print(f"Team A - {team_a}; Team B - {team_b}")
if condition:
    print("Game was terminated")
