number_of_heroes = int(input())
hero_name = dict()

for hero in range(number_of_heroes):
    hero_info = input().split()
    name = hero_info[0]
    health = int(hero_info[1])
    mana = int(hero_info[2])
    hero_name[name] = [health, mana]

while True:
    text = input()
    if text == 'End':
        break

    data = text.split(' - ')
    command = data[0]
    name = data[1]
    value = int(data[2])

    if command == 'CastSpell':
        spell_name = data[3]
        if hero_name[name][1] >= value:
            hero_name[name][1] -= value
            print(f"{name} has successfully cast {spell_name} and now has {hero_name[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command == 'TakeDamage':
        attacker = data[3]
        hero_name[name][0] -= value
        if hero_name[name][0] > 0:
            print(f"{name} was hit for {value} HP by {attacker} and now has {hero_name[name][0]} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del hero_name[name]

    elif command == 'Recharge':
        hero_name[name][1] += value
        if hero_name[name][1] > 200:
            diff = value - (hero_name[name][1] - 200)
            hero_name[name][1] = 200
            print(f"{name} recharged for {diff} MP!")
        else:
            print(f"{name} recharged for {value} MP!")

    elif command == 'Heal':
        if name in hero_name.keys():
            hero_name[name][0] += value
            if hero_name[name][0] > 100:
                diff = value - (hero_name[name][0] - 100)
                hero_name[name][0] = 100
                print(f"{name} healed for {diff} HP!")
            else:
                print(f"{name} healed for {value} HP!")

for name in hero_name.keys():
    print(name)
    print(f"HP: {hero_name[name][0]}")
    print(f"MP: {hero_name[name][1]}")
