number_of_locations = int(input())
gained_gold = 0
average_gain = 0

for i in range(number_of_locations):
    expected_gold_for_day = float(input())
    number_of_days = int(input())

    for u in range(number_of_days):
        gained_gold_for_day = float(input())

        gained_gold += gained_gold_for_day

    average_gain = gained_gold / number_of_days

    if average_gain >= expected_gold_for_day:
        print(f"Good job! Average gold per day: {average_gain:.2f}.")
    else:
        diff = abs(average_gain - expected_gold_for_day)
        print(f"You need {diff:.2f} gold.")

    gained_gold = 0
    average_gain = 0