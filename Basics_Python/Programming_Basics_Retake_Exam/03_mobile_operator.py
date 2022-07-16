duration_of_contract = input()
type_of_contract = input()
mobile_net = input()
months_for_payment = int(input())

if type_of_contract == 'Small':
    if duration_of_contract == 'one':
        price = 9.98
    elif duration_of_contract == 'two':
        price = 8.58

elif type_of_contract == 'Middle':
    if duration_of_contract == 'one':
        price = 18.99
    elif duration_of_contract == 'two':
        price = 17.09

elif type_of_contract == 'Large':
    if duration_of_contract == 'one':
        price = 25.98
    elif duration_of_contract == 'two':
        price = 23.59

elif type_of_contract == 'ExtraLarge':
    if duration_of_contract == 'one':
        price = 35.99
    elif duration_of_contract == 'two':
        price = 31.79

if mobile_net == 'yes':
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

total_price = price * months_for_payment

if duration_of_contract == 'two':
    total_price = total_price - (total_price * (3.75 / 100))

print(f"{total_price:.2f} lv.")