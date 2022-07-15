number_of_junior = int(input())
number_of_senior = int(input())
type_of_route = input()
junior_cost = 0
senior_cost = 0
all_number = 0
sum_cost = 0

all_number = number_of_junior + number_of_senior
if type_of_route == "trail":
    junior_cost = 5.50
    senior_cost = 7
elif type_of_route == "cross-country":
    if all_number >= 50:
        junior_cost = 8 - (8 * 0.25)
        senior_cost = 9.50 - (9.50 * 0.25)
    else:
        junior_cost = 8
        senior_cost = 9.50
elif type_of_route == "downhill":
    junior_cost = 12.25
    senior_cost = 13.75
elif type_of_route == "road":
    junior_cost = 20
    senior_cost = 21.50

sum_cost = number_of_junior * junior_cost + number_of_senior * senior_cost
sum_cost = sum_cost - (sum_cost * 0.05)
print(f'{sum_cost:.2f}')
