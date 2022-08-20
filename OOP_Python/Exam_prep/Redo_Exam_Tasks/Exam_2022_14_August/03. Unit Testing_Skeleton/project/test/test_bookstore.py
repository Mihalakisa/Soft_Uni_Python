from unittest import TestCase
from project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(1)

    def test_init(self):
        self.assertEqual(1, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_book_limit_error_bellow_zero(self):
        value = 0
        with self.assertRaises(ValueError) as error:
            self.bookstore = Bookstore(value)
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))

    def test_count_number_of_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'Axe': 1}
        self.assertEqual(len(self.bookstore.availability_in_store_by_book_titles), 1)
        self.assertEqual(self.bookstore.__len__(), 1)

        self.bookstore.availability_in_store_by_book_titles = {'Axe': 1, 'Shield': 1}
        self.assertEqual(len(self.bookstore.availability_in_store_by_book_titles), 2)
        self.assertEqual(self.bookstore.__len__(), 2)

    def test_receive_book_error_message_when_limit_is_reached(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Test', 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_if_there_is_enough_space_in_bookstore(self):
        book_name = 'Test'
        self.bookstore = Bookstore(10)
        result = self.bookstore.receive_book(book_name, 5)
        expected_string = f"{5} copies of {book_name} are available in the bookstore."
        self.assertEqual(result, expected_string)
        self.assertEqual(1, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertEqual(5, len(self.bookstore))
        result_second = self.bookstore.receive_book(book_name, 5)
        self.assertEqual(result_second, f"{10} copies of {book_name} are available in the bookstore.")
        self.assertEqual(1, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertEqual(10, len(self.bookstore))
        self.assertTrue(book_name in self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_string_number_of_copies(self):
        book_name = 'Test'
        number_of_books = 1
        result = self.bookstore.receive_book(book_name, number_of_books)
        expected_string = f"{number_of_books} copies of {book_name} are available in the bookstore."
        self.assertEqual(result, expected_string)
        self.assertEqual(len(self.bookstore), 1)

    def test_sell_book_error_msg_if_book_not_in_store(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Test', 1)
        self.assertEqual(f"Book Test doesn't exist!", str(error.exception))

    def test_sell_book_error_msg_if_not_enough_copies_to_sell(self):
        book_name = 'Test'
        number_of_books = 1
        self.bookstore.receive_book(book_name, number_of_books)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(book_name, 2)
        self.assertEqual(f"{book_name} has not enough copies to sell. Left: {number_of_books}", str(error.exception))

    def test_sell_book_successfully(self):
        self.bs = Bookstore(5)
        self.bs.receive_book('Title', 5)
        sell_book_example = self.bs.sell_book('Title', 3)
        self.assertEqual("Sold 3 copies of Title", sell_book_example)
        self.assertEqual(len(self.bs), 2)
        sell_book_example_two = self.bs.sell_book('Title', 2)
        self.assertEqual("Sold 2 copies of Title", sell_book_example_two)
        self.assertEqual(len(self.bs), 0)

    def test_str_msg(self):
        book_title = 'TestBook'
        number_of_copies = 1
        self.bookstore.receive_book(book_title, number_of_copies)
        self.bookstore.sell_book(book_title, number_of_copies)

        self.assertEqual(str(self.bookstore), f"Total sold books: 1\n"
                                       f"Current availability: 0\n"
                                       f" - {book_title}: 0 copies")
