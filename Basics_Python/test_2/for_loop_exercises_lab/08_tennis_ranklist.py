number_of_tournaments = int(input())
rank_list_points = int(input())
points = 0
wins = 0

for i in range(number_of_tournaments):
    stage_of_tournament = input()

    if stage_of_tournament == 'W':
        points += 2000
        wins += 1
    elif stage_of_tournament == 'F':
        points += 1200
    elif stage_of_tournament == 'SF':
        points += 720

final_points = rank_list_points + points
average_points = int(points / number_of_tournaments)
percent_wins = wins / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")