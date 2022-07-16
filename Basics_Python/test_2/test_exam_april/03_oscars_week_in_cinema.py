movie = input()
type_of_hall = input()
tickets_number = int(input())

if movie == 'A Star Is Born':
    if type_of_hall == 'normal':
        price = 7.50
    elif type_of_hall == 'luxury':
        price = 10.50
    elif type_of_hall == 'ultra luxury':
        price = 13.50

elif movie == 'Bohemian Rhapsody':
    if type_of_hall == 'normal':
        price = 7.35
    elif type_of_hall == 'luxury':
        price = 9.45
    elif type_of_hall == 'ultra luxury':
        price = 12.75

elif movie == 'Green Book':
    if type_of_hall == 'normal':
        price = 8.15
    elif type_of_hall == 'luxury':
        price = 10.25
    elif type_of_hall == 'ultra luxury':
        price = 13.25

elif movie == 'The Favourite':
    if type_of_hall == 'normal':
        price = 8.75
    elif type_of_hall == 'luxury':
        price = 11.55
    elif type_of_hall == 'ultra luxury':
        price = 13.95

sum = tickets_number * price

print(f"{movie} -> {sum:.2f} lv.")