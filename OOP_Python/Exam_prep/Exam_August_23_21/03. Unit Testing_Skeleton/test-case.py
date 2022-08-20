from project.library import Library

lib = Library('Test')
lib.add_book('ivan', 'batman')
lib.add_book('stefan', 'spiderman')
lib.add_reader('pesho')
lib.add_reader('ivailo')
print(lib.books_by_authors)
lib.rent_book('pesho', 'ivan', 'batman')

print(lib.readers)
print(lib.books_by_authors)