def multiplication(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return "negative"
    elif a == 0 or b == 0 or c == 0:
        return "zero"

    return "positive"


num1, num2, num3 = int(input()), int(input()), int(input())
print(multiplication(num1, num2, num3))
