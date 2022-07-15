def grades(num):
    if num < 3:
        return "Fail"
    elif num < 3.5:
        return "Poor"
    elif num < 4.5:
        return "Good"
    elif num < 5.5:
        return "Very Good"
    else:
        return "Excellent"


grade = float(input())
print(grades(grade))
