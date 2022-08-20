from unittest import TestCase

from project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def test_bookstore_init(self):
        self.bs = Bookstore(1)
        self.assertEqual(self.bs.books_limit, 1)
        self.assertEqual(self.bs.total_sold_books, 0)

    def test_books_limit_error_equal_to_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bs = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_books_limit_error_bellow_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bs = Bookstore(-1)
        self.assertEqual("Books limit of -1 is not valid", str(error.exception))

    def test_len_wrong_count(self):
        self.bs = Bookstore(1)
        self.bs.availability_in_store_by_book_titles = {'Axe': 1}
        self.assertEqual(self.bs.__len__(), 1)

    def test_len_not_addition(self):
        self.bs = Bookstore(2)
        self.bs.availability_in_store_by_book_titles = {'Axe': 1, 'Shield': 1}
        self.assertEqual(self.bs.__len__(), 2)

    def test_receive_book_if_there_is_not_enough_space(self):
        self.bs = Bookstore(1)
        with self.assertRaises(Exception) as error:
            self.bs.receive_book('Title', 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_if_there_is_enough_space_in_the_bookstore(self):
        self.bs = Bookstore(10)
        result = self.bs.receive_book('Title', 5)
        self.assertEqual("5 copies of Title are available in the bookstore.", result)
        self.assertEqual(len(self.bs), 5)
        result_second = self.bs.receive_book('Title', 5)
        self.assertEqual("10 copies of Title are available in the bookstore.", result_second)
        self.assertEqual(len(self.bs), 10)

    def test_sell_book_error_if_doesnt_exist(self):
        self.bs = Bookstore(2)
        self.bs.receive_book('Title', 1)
        with self.assertRaises(Exception) as error:
            self.bs.sell_book('Invalid', 1)
        self.assertEqual("Book Invalid doesn't exist!", str(error.exception))

    def test_sell_book_error_if_not_enough_copies(self):
        self.bs = Bookstore(2)
        self.bs.receive_book('Title', 1)
        with self.assertRaises(Exception) as error:
            self.bs.sell_book('Title', 2)
        self.assertEqual("Title has not enough copies to sell. Left: 1", str(error.exception))

    def test_sell_book_successfully(self):
        self.bs = Bookstore(5)
        self.bs.receive_book('Title', 5)
        sell_book_example = self.bs.sell_book('Title', 3)
        self.assertEqual("Sold 3 copies of Title", sell_book_example)
        self.assertEqual(len(self.bs), 2)
        sell_book_example_two = self.bs.sell_book('Title', 2)
        self.assertEqual("Sold 2 copies of Title", sell_book_example_two)
        self.assertEqual(len(self.bs), 0)

    def test_str_method(self):
        self.bs = Bookstore(5)
        self.bs.receive_book('Title', 5)
        sell_book_example = self.bs.sell_book('Title', 5)
        self.assertEqual("Sold 5 copies of Title", sell_book_example)

        self.assertEqual(str(self.bs), "Total sold books: 5\n"
                                       "Current availability: 0\n"
                                       " - Title: 0 copies")
