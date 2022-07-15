first_number = int(input())
second_number = int(input())
third_number = int(input())
second_prime = 0
first_n = 0
third_n = 0

for first in range(2, first_number + 1):
    for second in range(2, second_number + 1):
        for third in range(2, third_number + 1):

            if first % 2 == 0:
                first_n = first

            if third % 2 == 0:
                third_n = third

            if second_number % second == 0:
                pass
            else:
                second_prime = second

            print(f"{first_n} {second_prime} {third_n}")