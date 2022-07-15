points = 0
total_points = 0
winner_points = 0
winner_name = ''

while True:
    name = input()

    if name == 'Stop':
        print(f"The winner is {winner_name} with {winner_points} points!")
        break

    for ch in name:
        number = int(input())

        if ord(ch) == number:
            points += 10
        else:
            points += 2

    if points > winner_points:
        winner_points = points
        winner_name = name
    elif points == winner_points:
        winner_points = points
        winner_name = name

    points = 0