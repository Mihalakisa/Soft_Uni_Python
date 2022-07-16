def mover_rover(direction, row, col):
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def reposition_rover(row, col, size):
    if row < 0:
        return size - 1, col
    if row >= size:
        return 0, col
    if col < 0:
        return row, size - 1
    if col >= size:
        return row, 0


rover_row, rover_col = 0, 0

size = 6
area = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'E':
            rover_row, rover_col = row, col
    area.append(row_elements)

directions = input().split(', ')

water_found = False
metal_found = False
concrete_found = False

for direction in directions:
    rover_row, rover_col = mover_rover(direction, rover_row, rover_col)

    if is_outside(rover_row, rover_col, size):
        rover_row, rover_col = reposition_rover(rover_row, rover_col, size)

    cell_value = area[rover_row][rover_col]
    if cell_value == 'W':
        water_found = True
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    if cell_value == 'M':
        metal_found = True
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    if cell_value == 'C':
        concrete_found = True
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    if cell_value == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
