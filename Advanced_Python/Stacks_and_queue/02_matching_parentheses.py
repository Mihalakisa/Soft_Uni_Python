expression = input()

s = []

for i in range(len(expression)):
    if expression[i] == '(':
        s.append(i)
    elif expression[i] == ')':
        start_index = s.pop()
        end_index = i
        print(expression[start_index:end_index + 1])

'''
# Variants
Is expression valid?
    -stack should be empty at the end
    - Better to do the following:
        - when '(' +1
        - when ')' -1
        - 0 at the end

'''