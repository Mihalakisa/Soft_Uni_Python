football_team_name = input()
number_played_games = int(input())
win_count = 0
draw_count = 0
lose_count = 0
if number_played_games < 1:
    print(f"{football_team_name} hasn't played any games during this season.")
    exit()

for i in range(1, number_played_games + 1):
    result = input()

    if result == 'W':
        win_count += 1

    elif result == 'D':
        draw_count += 1

    elif result == 'L':
        lose_count += 1

all_points = win_count * 3 + draw_count
win_rate = (win_count / number_played_games) * 100

print(f"{football_team_name} has won {all_points} points during this season.")
print("Total stats:")
print(f"## W: {win_count}")
print(f"## D: {draw_count}")
print(f"## L: {lose_count}")
print(f"Win rate: {win_rate:.2f}%")