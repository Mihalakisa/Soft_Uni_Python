#   Кв. метри, които ще бъдат озеленени – реално число
square_meters_that_will_be_landscaped = float(input())
price_for_whole_yard = square_meters_that_will_be_landscaped * 7.61
discount = price_for_whole_yard * 0.18
result = price_for_whole_yard - discount

print(f"The final price is: {result} lv.")
print(f"The discount is: {discount} lv.")