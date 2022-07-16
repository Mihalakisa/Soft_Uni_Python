import sys

max_number = -sys.maxsize

while True:
    player_name = input()

    if player_name == 'END':
        break

    goals_scored = int(input())

    if goals_scored > max_number:
        max_number = goals_scored
        last_name = player_name

    if max_number >= 10:
        break

if max_number >= 10:
    print(f"{last_name} is the best player!")
    print(f"He has scored {max_number} goals and made a hat-trick !!!")
elif max_number >= 3:
    print(f"{last_name} is the best player!")
    print(f"He has scored {max_number} goals and made a hat-trick !!!")
elif max_number < 3:
    print(f"{last_name} is the best player!")
    print(f"He has scored {max_number} goals.")