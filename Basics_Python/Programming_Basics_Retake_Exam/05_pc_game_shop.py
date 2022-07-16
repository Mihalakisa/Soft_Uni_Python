number_sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(1, number_sold_games + 1):
    game = input()

    if game == 'Hearthstone':
        hearthstone += 1
    elif game == 'Fornite':
        fornite += 1
    elif game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

hearthstone = (hearthstone / number_sold_games) * 100
fornite = (fornite / number_sold_games) * 100
overwatch = (overwatch / number_sold_games) * 100
others = (others / number_sold_games) * 100
print(f"Hearthstone - {hearthstone:.2f}%")
print(f"Fornite - {fornite:.2f}%")
print(f"Overwatch - {overwatch:.2f}%")
print(f"Others - {others:.2f}%")