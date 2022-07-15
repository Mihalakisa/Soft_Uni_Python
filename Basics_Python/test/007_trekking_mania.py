number_of_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_sum_ppl = 0

for i in range(number_of_groups):
    number_of_ppl_in_group = int(input())
    total_sum_ppl += number_of_ppl_in_group

    if number_of_ppl_in_group <= 5:
        musala += number_of_ppl_in_group
    elif 6 <= number_of_ppl_in_group <= 12:
        monblan += number_of_ppl_in_group
    elif 13 <= number_of_ppl_in_group <= 25:
        kilimandjaro += number_of_ppl_in_group
    elif 26 <= number_of_ppl_in_group <= 40:
        k2 += number_of_ppl_in_group
    elif number_of_ppl_in_group >= 41:
        everest += number_of_ppl_in_group

musala = musala / total_sum_ppl * 100
monblan = monblan / total_sum_ppl * 100
kilimandjaro = kilimandjaro / total_sum_ppl * 100
k2 = k2 / total_sum_ppl * 100
everest = everest / total_sum_ppl * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimandjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")