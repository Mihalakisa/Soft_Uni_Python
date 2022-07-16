group_number = int(input())
all_ppl = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, group_number + 1):
    ppl_in_group = int(input())
    all_ppl += ppl_in_group

    if ppl_in_group <= 5:
        musala += ppl_in_group
    elif 6 <= ppl_in_group <= 12:
        monblan += ppl_in_group
    elif 13 <= ppl_in_group <= 25:
        kilimandjaro += ppl_in_group
    elif 26 <= ppl_in_group <= 40:
        k2 += ppl_in_group
    elif ppl_in_group >= 41:
        everest += ppl_in_group

musala = musala / all_ppl * 100
monblan = monblan / all_ppl * 100
kilimandjaro = kilimandjaro / all_ppl * 100
k2 = k2 / all_ppl * 100
everest = everest / all_ppl * 100
print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimandjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")