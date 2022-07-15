number_of_bitcoins = int(input())
number_of_ioana = float(input())
commission = float(input())

bitcoin = 1168
ioana = 0.15 * 1.76
euro = 1.95

sum = (bitcoin * number_of_bitcoins + ioana * number_of_ioana) / 1.95
sum_commission = sum * (commission / 100)
final = sum - sum_commission
print(f"{final:.2f}")