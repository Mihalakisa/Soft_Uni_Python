import sys
from collections import deque
from io import StringIO

# test_input_1 = '''10 16 13 25
# 12 11 8'''
# test_input_2 = '''10 14 22 4 5
# 11 16 17 11 1 8'''
# test_input_3 = '''5 6 7
# 2 1 5 7 5 3'''

# sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)

elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]

turns_count = 0
total_energy_spend = 0
toys_count = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    turns_count += 1
    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0
    if energy_to_be_spent <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spend += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factory)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)

print(f"Toys: {toys_count}")
print(f"Energy: {total_energy_spend}")
if elf_energies:
    elves_string = ', '.join(str(x) for x in elf_energies)
    print(f"Elves left: {elves_string}")
if boxes:
    boxes_string = ', '.join(str(x) for x in boxes)
    print(f"Boxes left: {boxes_string}")


    # if turns_count % 15 == 0 and (2 * box) <= elf_energy:
    #     toys_count += 0
    #     total_energy_spend += 2 * box
    #     elf_energies.append(elf_energy - (2 * box) + 0)
    # elif turns_count % 5 == 0 and box <= elf_energy:
    #     toys_count += 0
    #     total_energy_spend += 1 * box
    #     elf_energies.append(elf_energy - (1 * box) + 0)
    # elif turns_count % 3 == 0 and (2 * box) <= elf_energy:
    #     toys_count += 2
    #     total_energy_spend += 2 * box
    #     elf_energies.append(elf_energy - (2 * box) + 1)
    # elif box <= elf_energy and turns_count % 3 > 0:
    #     toys_count += 1
    #     total_energy_spend += 1 * box
    #     elf_energies.append(elf_energy - (1 * box) + 1)
    # else:
    #     boxes.append(box)
    #     elf_energies.append(elf_energy * 2)   # hot chocolate


# print(elf_energies, total_energy_spend, toys_count)
