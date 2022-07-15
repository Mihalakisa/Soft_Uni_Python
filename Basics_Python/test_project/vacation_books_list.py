page_numbers = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_per_day = (page_numbers / pages_per_hour) / number_of_days

print(round(hours_per_day))