width = int(input())
length = int(input())
number_of_pieces = width * length


while True:
    current_piece = input()

    if current_piece == 'STOP':
        break

    number_of_pieces -= int(current_piece)

    if number_of_pieces <= 0:
        break

if number_of_pieces <= 0:
    print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
else:
    print(f"{number_of_pieces} pieces are left.")