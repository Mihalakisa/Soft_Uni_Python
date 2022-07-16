class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

# class Book:
#     def __init__(self, title, author, publisher, image_url, price, short_desc):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.image_url = image_url
#         self.price = price
#         self.short_desc = short_desc
#
#
# book_1 = Book('Пътуване до дълбините на ума', 'Майкъл Полан', 'Изток - Запад', 'aaa.png', 25, 'Как новата наука за психеделиците променя представите ни за съзнанието')
# book_2 = Book('asd', 'me', 'me', 'bb.png', 15.90, 'asdr')
# basket = []
#
# basket.append(book_1)
# basket.append(book_2)
# total_price = 0
#
# for book in basket:
#     total_price += book.price
#
# print(total_price)