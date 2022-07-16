budget = float(input())
number_of_video_cards = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

sum_of_video_cards = number_of_video_cards * 250
price_for_cpu = sum_of_video_cards * 0.35
sum_of_cpu = number_of_cpu * price_for_cpu
price_of_ram = sum_of_video_cards * 0.1
sum_of_ram = number_of_ram * price_of_ram

total_sum = sum_of_video_cards + sum_of_cpu + sum_of_ram

if number_of_video_cards > number_of_cpu:
    total_sum = total_sum - total_sum * 0.15

diff = abs(budget - total_sum)
if total_sum <= budget:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')