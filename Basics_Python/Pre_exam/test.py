first_number = int(input())
second_number = int(input())
third_number = int(input())
second_prime = 0

for first in range(2, first_number + 1):
    for second in range(2, second_number + 1):
        for third in range(2, third_number + 1):

            if second == 2 or second == 3 or second == 5 or second == 7:

                if first % 2 == 0 and third % 2 == 0:

                    print(f"{first} {second} {third}")
