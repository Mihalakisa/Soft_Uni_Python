factor = int(input())
count = int(input())
multiples = 0
list_ = []

for x in range(count):
    multiples += factor
    list_.append(multiples)
print(list_)