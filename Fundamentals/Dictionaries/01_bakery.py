data = input().split(" ")
bakery = dict()  # --->  {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i+1]  # или (ако е число) ---> int(data[i+1])

    bakery[food] = int(quantity)

print(bakery)
