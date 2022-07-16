import math
number_of_persons = int(input())
capacity = int(input())

result = math.ceil(number_of_persons / capacity)

print(result)
