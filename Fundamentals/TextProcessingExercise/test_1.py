#  +---+---+---+---+---+
#  | m | o | v | i | e |
#  +---+---+---+---+---+
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1
# a = 'movie'
# print(a[-1])

# txt = 'H\te\tl\tl\to'  # това е TAB който разграничава буквите
# print(txt)
# text = 'Hello \bWorld!'  # приближава(връща) с един спейс(символ) назад
# print(text)
# text = 'Hello \nWorld!'  # прехвърля дума на нов ред
# print(text)

txt = 'Price is {price:.2f} dollars'
print(txt.format(price=199))

# print(''.join(reversed('123456789')))
# print('123456789' [::-1])

# test1 = 'abc'
# print(test1 * 3)
# print(test1 + ' Hello')

# # message = '       Hello Softuni     '
# # print(message.strip())
# message = 'Hello World!,,,'
# print(message.strip(','))

# sentence = 'this phrase is a string!'
# print(sentence[5:11])
# print(sentence[:4])
# print(sentence[-7:])

# text = 'Hello Softuni'
# print(text.title())     # Прави символите(буквите) на позиция 0 в главни букви
# print(text.swapcase())  # Заменя малките букви в големи а големите в малки

# text = 'Hello SoftUni fundamentals'
# print(text.find('fundamentals'))  # с find търсим от коя позиция(индекс) започва думата

# txt = '1, 2, 3, 4'
# print(txt.split(', '))

# a = 3.5
# b = str(a)
# print(type(b))

# text = 'This is text'
# text = "This is text"

# def test():
#     """
#     Аз съм
#     техт
#     на няколко реда
#     """
#     print('Welcome')
#
# print(test.__doc__)
