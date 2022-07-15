def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


player_1, player_2 = input().split(', ')

p1_wall_condition = False
p2_wall_condition = False

size = 6
matrix = []
count_turn = 0

for _ in range(size):
    matrix.append(input().split())

while True:
    count_turn += 1
    data = input().replace('(', '').replace(')', '').split(', ')
    player_row, player_col = int(data[0]), int(data[1])

    if is_inside(player_row, player_col, size):
        if count_turn % 2 != 0 and p1_wall_condition:
            p1_wall_condition = False
            continue
        elif count_turn % 2 == 0 and p2_wall_condition:
            p2_wall_condition = False
            continue

        if matrix[player_row][player_col] == 'E':
            if count_turn % 2 != 0:
                print(f"{player_1} found the Exit and wins the game!")
                break
            else:
                print(f"{player_2} found the Exit and wins the game!")
                break

        elif matrix[player_row][player_col] == 'T':
            if count_turn % 2 != 0:
                print(f"{player_1} is out of the game! The winner is {player_2}.")
                break
            else:
                print(f"{player_2} is out of the game! The winner is {player_1}.")
                break
        elif matrix[player_row][player_col] == 'W':
            if count_turn % 2 != 0:
                print(f"{player_1} hits a wall and needs to rest.")
                p1_wall_condition = True
            else:
                print(f"{player_2} hits a wall and needs to rest.")
                p2_wall_condition = True
