spell = input()
command = input()
final_spell = spell


while not command == "Abracadabra":
    command_input = command.split(" ")
    if command_input[0] == "Abjuration":
        final_spell = final_spell.upper()
        print(final_spell)
    elif command_input[0] == "Necromancy":
        final_spell = final_spell.lower()
        print(final_spell)
    elif command_input[0] == "Illusion":
        position = int(command_input[1])
        if position >= len(final_spell):
            print("The spell was too weak.")
        else:
            letter = command_input[2]
            final_spell = final_spell[:position]+letter+final_spell[position+1:]
            print("Done!")
    elif command_input[0] == "Diviation":
        find_word = command_input[1]
        if find_word in final_spell:
            replace_word = final_spell.find(command_input[1])
            final_spell = final_spell[0:replace_word]+command_input[2]
            print(final_spell)
    elif command_input[0] == "Alteration":
        find_word = command_input[1]
        if find_word in final_spell:
            replace_word = final_spell.find(command_input[1])
            final_spell = final_spell[0:replace_word]
            print(final_spell)
    else:
        print("The spell did not work!")

    command = input()
