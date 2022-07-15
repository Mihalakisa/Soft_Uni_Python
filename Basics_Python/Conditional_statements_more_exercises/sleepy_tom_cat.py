number_rest_days = int(input())

rest_days = number_rest_days * 127
work_days = (365 - number_rest_days) * 63
total_play_time = work_days + rest_days
sum_play_time = abs(30000 - total_play_time)

hour = sum_play_time // 60
minutes = sum_play_time % 60

if total_play_time < 30000:
    print('Tom sleeps well')
    print(f'{hour} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hour} hours and {minutes} minutes more for play')