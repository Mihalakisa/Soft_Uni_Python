rent = int(input())

figurines = rent - (rent * 0.30)
catering = figurines - (figurines * 0.15)
sound = 1/2 * catering

total_cost = rent + figurines + catering + sound
print(f"{total_cost:.2f}")
