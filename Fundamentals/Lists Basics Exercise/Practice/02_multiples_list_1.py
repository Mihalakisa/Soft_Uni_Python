factor = int(input())
count = int(input())
num_list = []
multiples = 0

for i in range(count):
    multiples += factor
    num_list.append(multiples)
print(num_list)
