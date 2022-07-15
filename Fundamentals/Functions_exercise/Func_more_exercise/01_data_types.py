def data_type(operation, num):
    if operation == "int":
        print(int(num) * 2)
    elif operation == "real":
        num = float(num) * 1.5
        print(f"{num:.2f}")
    elif operation == "string":
# print("${}$".format(num))
        print(f"${num}$")


current_operation = input()
number = input()
data_type(current_operation, number)
