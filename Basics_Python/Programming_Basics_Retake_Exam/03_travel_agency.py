city = input()
package_type = input()
vip_discount = input()
days_for_stay = int(input())

if city == 'Bansko' or city == 'Borovets':
    if package_type == 'withEquipment':
        price = 100
        if vip_discount == 'yes':
            price = price - (price * 0.1)
    elif package_type == 'noEquipment':
        price = 80
        if vip_discount == 'yes':
            price = price - (price * 0.05)
    else:
        print("Invalid input!")
        exit()

elif city == 'Varna' or city == 'Burgas':
    if package_type == 'withBreakfast':
        price = 130
        if vip_discount == 'yes':
            price = price - (price * 0.12)
    elif package_type == 'noBreakfast':
        price = 100
        if vip_discount == 'yes':
            price = price - (price * 0.07)
    else:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")
    exit()

if days_for_stay < 1:
    print("Days must be positive number!")
    exit()

if days_for_stay > 7:
    days_for_stay -= 1

final_sum = days_for_stay * price
print(f"The price is {final_sum:.2f}lv! Have a nice time!")