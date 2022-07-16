fruit = input()
size_of_set = input()
number_of_set = int(input())
prize = 0
final_prize = 0

if fruit == 'Watermelon':
    if size_of_set == 'small':
        prize = 2 * 56
        prize *= number_of_set
    elif size_of_set == 'big':
        prize = 5 * 28.70
        prize *= number_of_set

elif fruit == 'Mango':
    if size_of_set == 'small':
        prize = 2 * 36.66
        prize *= number_of_set
    elif size_of_set == 'big':
        prize = 5 * 19.60
        prize *= number_of_set

elif fruit == 'Pineapple':
    if size_of_set == 'small':
        prize = 2 * 42.10
        prize *= number_of_set
    elif size_of_set == 'big':
        prize = 5 * 24.80
        prize *= number_of_set

elif fruit == 'Raspberry':
    if size_of_set == 'small':
        prize = 2 * 20
        prize *= number_of_set
    elif size_of_set == 'big':
        prize = 5 * 15.20
        prize *= number_of_set

if 400 <= prize <= 1000:
    final_prize = prize - (prize * 0.15)
    print(f"{final_prize:.2f} lv.")
elif prize > 1000:
    final_prize = prize - (prize * 0.5)
    print(f"{final_prize:.2f} lv.")
else:
    print(f"{prize:.2f} lv.")
