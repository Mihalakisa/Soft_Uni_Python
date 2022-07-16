from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_counter = 0
crashed = False

while not crashed:
    line = input()

    if line == 'END':
        break

    if line == 'green':
        current_green = green_light
        while cars and current_green > 0:
            car = cars.popleft()
            if len(car) <= current_green + free_window:
                passed_counter += 1
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_green + free_window]}.")
                crashed = True
                break
            current_green -= len(car)
    else:
        cars.append(line)

if not crashed:
    print("Everyone is safe.")
    print(f"{passed_counter} total cars passed the crossroads.")