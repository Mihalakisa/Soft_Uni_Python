count_days = 1
sum_meters = 0
sum_meters += 5364

while True:

    spends_the_night = input()

    if spends_the_night == 'END':
        print(f"Failed!")
        print(f"{sum_meters}")
        break

    climbed_meters = int(input())

    if spends_the_night == 'Yes':
        count_days += 1
        if count_days > 5:
            print(f"Failed!")
            print(f"{sum_meters}")
            break
        sum_meters += climbed_meters

    elif spends_the_night == 'No':
        sum_meters += climbed_meters

    if sum_meters >= 8848:
        print(f"Goal reached for {count_days} days!")
        break
