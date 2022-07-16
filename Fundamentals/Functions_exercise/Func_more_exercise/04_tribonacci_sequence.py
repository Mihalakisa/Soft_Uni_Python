def tribonacci(number):
    list_of_three = [1, 1, 2]
    result = "1 1 2"
    for x in range(3, number):
        sum_list = sum(list_of_three)
        result += " " + str(sum_list)
        list_of_three.append(sum_list)
        list_of_three.remove(list_of_three[0])
    return result


cycles = int(input())
print(tribonacci(cycles))