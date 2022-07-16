game_list = input()
explode = [game.split(' ') for game in game_list.split('|')]
health = 100
coins = 0
room = 0
condition = True
damaged = 0
diff = 0

for game in range(len(explode)):
    command = explode[game][0]
    number = explode[game][1]
    room += 1
    damaged = health

    if command == 'potion':
        health += int(number)
        if health > 100:
            diff = 100 - damaged
            health = 100
            print(f"You healed for {diff} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")

    elif command == 'chest':
        coins += int(number)
        print(f"You found {number} bitcoins.")

    else:
        if health > 0:
            health -= int(number)
            if health <= 0:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {room}")
                condition = False
                break
            else:
                print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            condition = False
            break

if condition:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
