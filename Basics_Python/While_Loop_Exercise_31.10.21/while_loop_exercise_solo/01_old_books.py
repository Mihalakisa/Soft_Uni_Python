book = input()
search_book = input()
count = 0

while search_book != book:

    if search_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break
    count += 1
    search_book = input()

else:
    print(f"You checked {count} books and found it.")