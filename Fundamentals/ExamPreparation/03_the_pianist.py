number_of_pieces = int(input())
piece_dict = dict()

for i in range(number_of_pieces):
    text = input().split('|')
    piece = text[0]
    composer = text[1]
    key = text[2]
    piece_dict[piece] = [composer, key]

while True:
    text = input()
    if text == 'Stop':
        break
    data = text.split('|')
    command = data[0]
    piece = data[1]

    if command == 'Add':
        composer = data[2]
        key = data[3]
        if piece not in piece_dict.keys():
            piece_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == 'Remove':
        if piece not in piece_dict.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del piece_dict[piece]
            print(f"Successfully removed {piece}!")

    elif command == 'ChangeKey':
        new_key = data[2]
        if piece in piece_dict.keys():
            piece_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece in piece_dict.keys():
    print(f"{piece} -> Composer: {piece_dict[piece][0]}, Key: {piece_dict[piece][1]}")
