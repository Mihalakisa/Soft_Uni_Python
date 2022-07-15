number_of_joinery = int(input())
type_of_joinery = input()
shipment_method = input()

if type_of_joinery == "90X130":
    price = number_of_joinery * 110
    if number_of_joinery < 10:
        print("Invalid order")
    elif 10 < number_of_joinery <= 30:
        print(f'{price:.2f} BGN')
    elif 30 < number_of_joinery <= 60:
        price = price - price * 0.05
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 60 < number_of_joinery <= 99:
        price = price - price * 0.08
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 99 < number_of_joinery:
        price = price - price * 0.08
        if shipment_method == "With delivery":
            price = price + 60
            price = price - price * 0.04
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            price = price - price * 0.04
            print(f'{price:.2f} BGN')

elif type_of_joinery == "100X150":
    price = number_of_joinery * 140
    if number_of_joinery < 10:
        print("Invalid order")
    elif 10 < number_of_joinery <= 40:
        print(f'{price:.2f} BGN')
    elif 40 < number_of_joinery <= 80:
        price = price - price * 0.06
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 80 < number_of_joinery <= 99:
        price = price - price * 0.1
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 99 < number_of_joinery:
        price = price - price * 0.1
        if shipment_method == "With delivery":
            price = price + 60
            price = price - price * 0.04
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            price = price - price * 0.04
            print(f'{price:.2f} BGN')

elif type_of_joinery == "130X180":
    price = number_of_joinery * 190
    if number_of_joinery < 10:
        print("Invalid order")
    elif 10 < number_of_joinery <= 20:
        print(f'{price:.2f} BGN')
    elif 20 < number_of_joinery <= 50:
        price = price - price * 0.07
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 50 < number_of_joinery <= 99:
        price = price - price * 0.12
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 99 < number_of_joinery:
        price = price - price * 0.12
        if shipment_method == "With delivery":
            price = price + 60
            price = price - price * 0.04
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            price = price - price * 0.04
            print(f'{price:.2f} BGN')

elif type_of_joinery == "200X300":
    price = number_of_joinery * 250
    if number_of_joinery < 10:
        print("Invalid order")
    elif 10 < number_of_joinery <= 25:
        print(f'{price:.2f} BGN')
    elif 25 < number_of_joinery <= 50:
        price = price - price * 0.09
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 50 < number_of_joinery <= 99:
        price = price - price * 0.14
        if shipment_method == "With delivery":
            price = price + 60
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            print(f'{price:.2f} BGN')
    elif 99 < number_of_joinery:
        price = price - price * 0.14
        if shipment_method == "With delivery":
            price = price + 60
            price = price - price * 0.04
            print(f'{price:.2f} BGN')
        elif shipment_method == "Without delivery":
            price = price - price * 0.04
            print(f'{price:.2f} BGN')