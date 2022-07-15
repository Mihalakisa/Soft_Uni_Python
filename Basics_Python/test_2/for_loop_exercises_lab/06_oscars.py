actor_name = input()
academy_points = float(input())
raters = int(input())
sum = academy_points

for i in range(raters):
    rater_name = input()
    rater_points = float(input())

    sum += ((len(rater_name) * rater_points) / 2)

    if sum >= 1250.5:
        break

if sum >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {sum:.1f}!")
else:
    diff = 1250.5 - sum
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")