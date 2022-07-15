from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

mix_result = 0
datura_bomb = 0
cherry_bomb = 0
smoke_decoy = 0

while bomb_effects and bomb_casings:
    current_b_effect = bomb_effects[0]
    current_b_casting = bomb_casings[-1]

    if datura_bomb >= 3 and cherry_bomb >= 3 and smoke_decoy >= 3:
        break

    mix_result = current_b_effect + current_b_casting

    if mix_result == 40:
        datura_bomb += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif mix_result == 60:
        cherry_bomb += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif mix_result == 120:
        smoke_decoy += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if datura_bomb >= 3 and cherry_bomb >= 3 and smoke_decoy >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print(f"Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bomb}")
print(f"Datura Bombs: {datura_bomb}")
print(f"Smoke Decoy Bombs: {smoke_decoy}")
