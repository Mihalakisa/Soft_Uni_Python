months = int(input())
el_sum = 0
water = 0
internet = 0
others = 0
final_others = 0

for i in range(months):
    electricity_cost = float(input())

    el_sum += electricity_cost
    water += 20
    internet += 15
    others += electricity_cost + 20 + 15
    final_others = others + (others * 20/100)

average_sum = (el_sum + water + internet + final_others) / months

print(f"Electricity: {el_sum:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {final_others:.2f} lv")
print(f"Average: {average_sum:.2f} lv")