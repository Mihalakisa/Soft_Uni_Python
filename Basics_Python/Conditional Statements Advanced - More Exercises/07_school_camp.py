season = input()
group = input()
number_of_students = int(input())
number_of_nights = int(input())
price = 0

if number_of_students < 10:
    if season == 'Winter':
        if group == 'girls':
            price = number_of_students * number_of_nights * 9.60
            print(f"Gymnastics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 9.60
            print(f"Judo {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 10
            print(f"Ski {price:.2f} lv.")
    elif season == 'Spring':
        if group == 'girls':
            price = number_of_students * number_of_nights * 7.20
            print(f"Athletics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 7.20
            print(f"Tennis {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 9.50
            print(f"Cycling {price:.2f} lv.")
    elif season == 'Summer':
        if group == 'girls':
            price = number_of_students * number_of_nights * 15
            print(f"Volleyball {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 15
            print(f"Football {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 20
            print(f"Swimming {price:.2f} lv.")

elif 10 <= number_of_students < 20:
    if season == 'Winter':
        if group == 'girls':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.05)
            print(f"Gymnastics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.05)
            print(f"Judo {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 10
            price = price - (price * 0.05)
            print(f"Ski {price:.2f} lv.")
    elif season == 'Spring':
        if group == 'girls':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.05)
            print(f"Athletics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.05)
            print(f"Tennis {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 9.50
            price = price - (price * 0.05)
            print(f"Cycling {price:.2f} lv.")
    elif season == 'Summer':
        if group == 'girls':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.05)
            print(f"Volleyball {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.05)
            print(f"Football {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 20
            price = price - (price * 0.05)
            print(f"Swimming {price:.2f} lv.")

elif 20 <= number_of_students < 50:
    if season == 'Winter':
        if group == 'girls':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.15)
            print(f"Gymnastics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.15)
            print(f"Judo {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 10
            price = price - (price * 0.15)
            print(f"Ski {price:.2f} lv.")
    elif season == 'Spring':
        if group == 'girls':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.15)
            print(f"Athletics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.15)
            print(f"Tennis {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 9.50
            price = price - (price * 0.15)
            print(f"Cycling {price:.2f} lv.")
    elif season == 'Summer':
        if group == 'girls':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.15)
            print(f"Volleyball {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.15)
            print(f"Football {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 20
            price = price - (price * 0.15)
            print(f"Swimming {price:.2f} lv.")

elif number_of_students >= 50:
    if season == 'Winter':
        if group == 'girls':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.5)
            print(f"Gymnastics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 9.60
            price = price - (price * 0.5)
            print(f"Judo {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 10
            price = price - (price * 0.5)
            print(f"Ski {price:.2f} lv.")
    elif season == 'Spring':
        if group == 'girls':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.5)
            print(f"Athletics {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 7.20
            price = price - (price * 0.5)
            print(f"Tennis {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 9.50
            price = price - (price * 0.5)
            print(f"Cycling {price:.2f} lv.")
    elif season == 'Summer':
        if group == 'girls':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.5)
            print(f"Volleyball {price:.2f} lv.")
        elif group == 'boys':
            price = number_of_students * number_of_nights * 15
            price = price - (price * 0.5)
            print(f"Football {price:.2f} lv.")
        elif group == 'mixed':
            price = number_of_students * number_of_nights * 20
            price = price - (price * 0.5)
            print(f"Swimming {price:.2f} lv.")