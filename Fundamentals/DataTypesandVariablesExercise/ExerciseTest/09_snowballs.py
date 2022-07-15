import sys

num = int(input())
max_num = -sys.maxsize

for i in range(num):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    result = (snowball_weight / snowball_time) ** snowball_quality
    if result > max_num:
        max_num = result
        current_weight = snowball_weight
        current_time = snowball_time
        current_quality = snowball_quality

print(f"{current_weight} : {current_time} = {int(max_num)} ({current_quality})")
