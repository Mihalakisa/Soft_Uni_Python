import math

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
gift_price = float(input())

total_sum = number_of_magnolias * 3.25 + number_of_hyacinths * 4 + number_of_roses * 3.5 + number_of_cacti * 8
taxes = 5/100 * total_sum
profit = total_sum - taxes

if profit < gift_price:
    diff = math.ceil(gift_price - profit)
    print(f'She will have to borrow {diff} leva.')
else:
    diff = math.floor(profit - gift_price)
    print(f'She is left with {diff} leva.')