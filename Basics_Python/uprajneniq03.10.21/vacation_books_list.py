# 1. Входни данни -> бр. страници (int), стр. за час (int), дни (int)
# 2. Часове за прочитане = бр. страници / стр. за час
# 3. Часове на ден = часове за прочитане / дни
# 4. Отпечатваме часове на ден

count_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

total_hours_reading = count_pages // pages_per_hour
hours_per_day = total_hours_reading / days_for_reading
print(hours_per_day)