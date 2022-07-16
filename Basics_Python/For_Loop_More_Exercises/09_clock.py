import time
import random

hour = random.randrange(0, 23)
minute = random.randrange(0, 60)
second = random.randrange(0, 60)

while (hour < 24):
    while (minute < 60):
        while (second < 60):
            second += 1
            time.sleep(1)
            print(str(hour) + ":" + str(minute) + ":" + str(second))

        second = 0
        minute += 1

    minute = 0
    hour += 1