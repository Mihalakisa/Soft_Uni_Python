stadium_capacity = int(input())
number_of_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for i in range(number_of_fans):
    sector = input()

    if sector == 'A':
        fans_a += 1
    elif sector == 'B':
        fans_b += 1
    elif sector == 'V':
        fans_v += 1
    elif sector == 'G':
        fans_g += 1

percent_a = fans_a / number_of_fans * 100
percent_b = fans_b / number_of_fans * 100
percent_v = fans_v / number_of_fans * 100
percent_g = fans_g / number_of_fans * 100
all_fans = number_of_fans / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{all_fans:.2f}%")