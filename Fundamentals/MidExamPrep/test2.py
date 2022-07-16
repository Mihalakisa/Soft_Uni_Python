def calculation(number):
    price_no_tax = 0
    price_no_tax += float(number)
    taxes = price_no_tax * (20 / 100)
    total_price = taxes + price_no_tax
    return total_price


def command_result(operation):
    if operation == 'special':
        special_result = calculation(command) - (calculation(command) * 0.1)
        return special_result
    elif operation == 'regular':
        return operation


command = input()
if command.isdigit():
    calculation(command)
if command.isalpha():
    command_result(calculation)

print(command_result(calculation(command)))
