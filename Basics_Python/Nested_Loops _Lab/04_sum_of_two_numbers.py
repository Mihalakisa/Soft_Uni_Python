start_number = int(input())
end_number = int(input())
magic_number = int(input())
count = 0

for start in range(1, start_number + 1):
    for end in range(1, end_number + 1):
        count += 1
        if start + end == magic_number:
            break
if start + end == magic_number:
    print(f"Combination N:{count} ({start} + {end} = {magic_number})")
else:
    print(f"{count} combinations - neither equals {magic_number}")