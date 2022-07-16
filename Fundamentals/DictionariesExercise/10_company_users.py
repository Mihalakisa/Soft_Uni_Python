company_dict = {}

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(' -> ')
    company_name = data[0]
    employee_id = data[1]

    if company_name not in company_dict:
        company_dict[company_name] = []
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)
    else:
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)

for company in company_dict:
    print(company)
    for id in company_dict[company]:
        print(f"-- {id}")