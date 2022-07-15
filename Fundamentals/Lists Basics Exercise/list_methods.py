# LIST METHODS
# append() - добавя в информация в листа
# clear() - изтрива всичко в листа
# copy() - копира листа( запазва структурата на оригиналния лист и обработваме само копието)
# count() - взима бройката на повтарящи се елементи в листа
# extend() - обединява (събира 2 или повече списъка в 1)
# index() - стойност на индекса пример -> index = (i for i, value in enumerate(fruits) if value == 'apple')
# //// print(list(index))
# insert() - поставяме елемент на определено място/ позиция ( fruits.insert(1, 'orange') )
# pop() - попваме или махаме първия елемент по индекс/ примерно list.pop(0)
# remove() - премахва специфичен елемент
# reverse() - обръща от зад напред списъка
# sort() - сортира самия лист(подрежда по азбучен ред)

test_list = [3, 'test', True, int, float]
print(test_list)

numbers = list(range(0, 11, 1))
print(numbers)

# fruits = ['apple', 'banana', 'kiwi']
# print(' '.join(fruits))

fruits = input().split(', ')
print(fruits)
# split разделя елементи а join обединява

# alphabets = input().split(', ')
# print('.....'.join(alphabets))
