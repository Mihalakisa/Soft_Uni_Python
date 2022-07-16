deck = input().split(' ')
shuffles = int(input())
count_deck = 0
shuffled_deck = []

while count_deck < shuffles:
    first_half = []
    second_half = []
    count_card = 0
    shuffled_deck = []

    for card in deck:
        count_card += 1
        if count_card <= len(deck) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    for number in range(int(len(deck) / 2)):
        shuffled_deck.append(first_half[number])
        shuffled_deck.append(second_half[number])
    deck = shuffled_deck
    count_deck += 1

print(shuffled_deck)