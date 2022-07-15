name_of_actor = input()
points_from_academy = float(input())
number_of_rate = int(input())
total_points = points_from_academy

for i in range(number_of_rate):
    name_of_rater = input()
    points_from_rater = float(input())

    total_points = total_points + ((len(name_of_rater) * points_from_rater) / 2)

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")