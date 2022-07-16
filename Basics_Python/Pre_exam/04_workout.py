import math

number_of_days = int(input())
number_of_km = float(input())
sum_km = 0
sum_km += number_of_km
total_km = 0
total_km += number_of_km

for i in range(number_of_days):
    percent_per_day = int(input())

    sum_km += (sum_km * (percent_per_day / 100))
    total_km += sum_km

diff = abs(total_km - 1000)
if total_km >= 1000:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")