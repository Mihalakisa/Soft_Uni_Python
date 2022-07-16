import re

# text = 'The movie was Scary'
# result = re.search(r'^The.*Scary$', text)
# text = 'The weather in Spain is nice'
# result = re.findall(r'in', text)
# result = re.split(r'\s', text)
# print(result)

text = 'The price of OLIVEOIL is 4 leva'
result = re.search(r'(\b[A-Z]+\b).+(\b\d+)', text)
print(result.groups())
print(result.group(1))
print(result.group(2))