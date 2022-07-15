animals = input().split(", ")

count = len(animals)

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    for animal in animals:
        count -= 1
        if animal == "wolf":
            print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")
            break