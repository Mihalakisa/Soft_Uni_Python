number_of_lines = int(input())
start_bracket = 0
end_bracket = 0
last_bracket = ')'

for i in range(number_of_lines):
    random_string = input()

    if random_string == '(':
        start_bracket += 1
    if random_string == ')':
        end_bracket += 1
    if random_string == '(' or random_string == ')':
        if random_string != last_bracket:
            last_bracket = random_string
        else:
            print("UNBALANCED")
            exit()

if start_bracket == end_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
