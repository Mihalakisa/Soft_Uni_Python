easter_cakes_number = int(input())
points = 0
win_points = 0
baker = ''

for i in range(1, easter_cakes_number + 1):
    baker_name = input()
    while True:
        easter_cakes_rating = input()

        if easter_cakes_rating == 'Stop':
            print(f"{baker_name} has {points} points.")
            if points > win_points:
                win_points = points
                win_name = baker_name
                print(f"{baker_name} is the new number 1!")
            points = 0
            break

        points += int(easter_cakes_rating)

print(f"{win_name} won competition with {win_points} points!")