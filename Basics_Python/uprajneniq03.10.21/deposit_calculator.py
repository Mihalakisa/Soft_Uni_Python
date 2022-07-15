# 1. входни данни -> депозирана сума (float), срок (int), процент (float)
# 2. изчисляваме крайната съма
# 3. отпечатваме крайната сума
deposit_sum = float(input())
months = int(input())
percent = float(input())

# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
final_sum = deposit_sum + months * ((deposit_sum * (percent/100)) / 12)
print(final_sum)