travel_stops = input()

while True:
    text = input()

    if text == 'Travel':
        print(f"Ready for world tour! Planned stops: {travel_stops}")
        break

    data = text.split(':')
    command = data[0]
    index = data[1]
    string = data[2]

    if command == 'Add Stop':
        travel_stops = travel_stops[:int(index)] + f'{string}' + travel_stops[int(index):]

    elif command == 'Remove Stop':
        if int(index) < len(travel_stops) and int(string) < len(travel_stops):
            travel_stops = travel_stops[0:int(index):] + travel_stops[int(string) + 1::]

    elif command == 'Switch':
        if index in travel_stops:
            travel_stops = travel_stops.replace(index, string)

    print(travel_stops)
