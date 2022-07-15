bought_food = int(input()) * 1000
total_eaten_food = 0

while True:
    eaten_food = input()

    if eaten_food == 'Adopted':
        if bought_food >= total_eaten_food:
            final_result = abs(bought_food - total_eaten_food)
            print(f"Food is enough! Leftovers: {final_result} grams.")
            break
        else:
            final_result = abs(bought_food - total_eaten_food)
            print(f"Food is not enough. You need {final_result} grams more.")
            break

    total_eaten_food += int(eaten_food)