player_one_eggs = int(input())
player_two_eggs = int(input())

while True:
    winner = input()

    if winner == 'End of battle':
        print(f"Player one has {player_one_eggs} eggs left.")
        print(f"Player two has {player_two_eggs} eggs left.")
        break

    if winner == 'one':
        player_two_eggs -= 1
        if player_two_eggs == 0:
            print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
            break

    elif winner == 'two':
        player_one_eggs -= 1
        if player_one_eggs == 0:
            print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
            break