number_of_groups = int(input())
count_ppl = 0
musala= 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0


for i in range(number_of_groups):
    number_of_ppl = int(input())
    count_ppl += number_of_ppl

    if number_of_ppl <= 5:
        musala += number_of_ppl
    elif 6 <= number_of_ppl <= 12:
        monblan += number_of_ppl
    elif 13 <= number_of_ppl <= 25:
        kilimandjaro += number_of_ppl
    elif 26 <= number_of_ppl <= 40:
        k2 += number_of_ppl
    elif number_of_ppl >= 41:
        everest += number_of_ppl

musala = (musala / count_ppl) * 100
monblan = (monblan / count_ppl) * 100
kilimandjaro = (kilimandjaro / count_ppl) * 100
k2 = (k2 / count_ppl) * 100
everest = (everest / count_ppl) * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimandjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")