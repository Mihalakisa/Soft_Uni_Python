start_number = int(input())
end_number = int(input())
magic_number = int(input())
count = 0
is_found = False

for start in range(start_number, end_number + 1):
    for end in range(start_number, end_number + 1):
        count += 1
        if start + end == magic_number:
            print(f"Combination N:{count} ({start} + {end} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
else:
    print(f"{count} combinations - neither equals {magic_number}")