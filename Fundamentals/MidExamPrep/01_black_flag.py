days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder_sum = 0


for day in range(1, days + 1):

    plunder_sum += daily_plunder

    if day % 3 == 0:
        plunder_sum += daily_plunder * 0.5

    if day % 5 == 0:
        plunder_sum -= plunder_sum * 0.3


if plunder_sum >= expected_plunder:
    print(f"Ahoy! {plunder_sum:.2f} plunder gained.")

else:
    percent_plunder = (plunder_sum / expected_plunder) * 100
    print(f"Collected only {percent_plunder:.2f}% of the plunder.")
