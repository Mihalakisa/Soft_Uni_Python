name_of_actor = input()
points_from_academy = float(input())
number_of_evaluators = int(input())
total_points = points_from_academy

for _ in range(number_of_evaluators):
    name_of_evaluators = input()
    points_from_evaluators = float(input())

    total_points += ((len(name_of_evaluators) * points_from_evaluators) / 2)

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(1250.5 - total_points)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')