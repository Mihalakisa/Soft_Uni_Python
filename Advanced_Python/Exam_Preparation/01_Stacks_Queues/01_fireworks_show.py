from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

mixed_sum = 0
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects and explosive_power:
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        break
    firework = firework_effects.popleft()
    explosive = explosive_power.pop()

    if firework > 0 and explosive > 0:

        mixed_sum = firework + explosive

        if mixed_sum % 3 == 0 and not mixed_sum % 5 == 0:
            palm_fireworks += 1
        elif not mixed_sum % 3 == 0 and mixed_sum % 5 == 0:
            willow_fireworks += 1
        elif mixed_sum % 3 == 0 and mixed_sum % 5 == 0:
            crossette_fireworks += 1
        else:
            firework -= 1
            firework_effects.append(firework)
            explosive_power.append(explosive)
    else:
        if 0 >= firework and 0 >= explosive:
            continue
        elif 0 >= firework:
            explosive_power.append(explosive)
        elif 0 >= explosive:
            firework_effects.appendleft(firework)

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
