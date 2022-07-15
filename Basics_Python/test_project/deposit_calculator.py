#   Депозирана сума
deposit_number = float(input())
#   Срок на депозита
deposit_term = int(input())
#   годишен лихвен процент
annual_rate = float(input())

a = deposit_number * annual_rate / 100
b = a / 12
amount = deposit_number + deposit_term * b


print(amount)