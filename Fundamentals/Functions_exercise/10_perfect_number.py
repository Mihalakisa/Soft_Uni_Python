def perfect_num(num):
    sum_result = 0
    for i in range(1, num):
        if num % i == 0:
            sum_result += i

    if sum_result == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_num(number))
