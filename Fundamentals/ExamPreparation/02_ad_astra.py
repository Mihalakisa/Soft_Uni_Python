import math
import re

text = input()
result_list = []
day_calories = 0
day_count = 0

# pattern = r'(\#|\|)[A-Z][a-z]+\1[0-9][1-9](\/[0-9][0-9])*(\#|\|)[0-9]+\3'
# pattern = r'(\#|\|)(?P<item>[A-Z][a-z]+)\1(?P<date>[0-9][1-9](\/[0-9][0-9]){2})(\#|\|)(?P<calories>[0-9]+)\5'
pattern = r'(\#|\|)(?P<item>[A-Z][a-z]+( [A-Z][a-z]+)*)\1(?P<date>[0-9][1-9](\/[0-9][0-9]){2})(\#|\|)(?P<calories>[0-9]+)\6'
result = re.finditer(pattern, text)

for day in result:
    calories = day.group("calories")
    day_calories += int(calories)

day_count = math.floor(day_calories / 2000)

print(f"You have food to last you for: {day_count} days!")

result = re.finditer(pattern, text)

for match in result:
    item = match.group("item")
    date = match.group("date")
    calories = match.group("calories")

    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
