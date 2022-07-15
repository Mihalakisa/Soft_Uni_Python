first_number = input()
second_number = input()

for one in range(int(first_number[0]), int(second_number[0]) + 1):
    for two in range(int(first_number[1]), int(second_number[1]) + 1):
        for three in range(int(first_number[2]), int(second_number[2]) + 1):
            for four in range(int(first_number[3]), int(second_number[3]) + 1):
                if one % 2 != 0 and two % 2 != 0 and three % 2 != 0 and four % 2 != 0:
                    print(f"{one}{two}{three}{four}", end=' ')