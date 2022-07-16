trunk_capacity = float(input())
total_size_sum = 0
count_suitcase = 0
count = 0

while True:
    size_of_suitcase = input()
    count += 1
    if size_of_suitcase == 'End':
        break

    if count % 3 == 0:
        size_of_suitcase = float(size_of_suitcase) + (float(size_of_suitcase) * 0.1)
        total_size_sum += size_of_suitcase
    else:
        total_size_sum += float(size_of_suitcase)

    if total_size_sum > trunk_capacity:
        break

    count_suitcase += 1

if trunk_capacity >= total_size_sum:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {count_suitcase} suitcases loaded.")

else:
    print("No more space!")
    print(f"Statistic: {count_suitcase} suitcases loaded.")
