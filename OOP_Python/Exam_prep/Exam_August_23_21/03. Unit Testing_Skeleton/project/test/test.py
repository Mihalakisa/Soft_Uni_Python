from unittest import TestCase
from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.lib = Library('Test')

    def test_library_init(self):
        self.assertEqual(self.lib.name, 'Test')
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_if_name_is_empty_string_returns_error(self):
        with self.assertRaises(ValueError) as error:
            self.lib = Library('')
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book(self):
        author = 'Author'
        first_title = 'Title1'
        second_title = 'Title2'
        self.lib.add_book(author, first_title)
        self.lib.add_book(author, first_title)
        self.lib.add_book(author, second_title)

        self.assertEqual(1, len(self.lib.books_by_authors))
        self.assertTrue(author in self.lib.books_by_authors)
        self.assertEqual([first_title, second_title], self.lib.books_by_authors[author])

    def test_add_reader_should_add_reader(self):
        reader_name = 'Reader'
        self.lib.add_reader(reader_name)
        self.assertEqual(1, len(self.lib.readers))
        self.assertTrue(reader_name in self.lib.readers)
        self.assertEqual([], self.lib.readers[reader_name])

    def test_add_reader_should_return_error_msg_when_reader_is_already_registered(self):
        reader_name = 'Reader'
        self.lib.add_reader(reader_name)

        result = self.lib.add_reader(reader_name)
        expected_result = f"{reader_name} is already registered in the Test library."

        self.assertEqual(result, expected_result)

    def test_rent_book_should_return_error_message_when_reader_is_not_registered(self):
        reader_name = 'reader'
        result = self.lib.rent_book(reader_name, 'author', 'title')
        expected_result = f"{reader_name} is not registered in the {self.lib.name} Library."

        self.assertEqual(result, expected_result)

    def test_rent_book_should_return_error_message_when_author_is_not_registered(self):
        reader_name = 'reader'
        author_name = 'author'
        self.lib.add_reader(reader_name)

        result = self.lib.rent_book(reader_name, author_name, 'title')
        expected_result = f"{self.lib.name} Library does not have any {author_name}'s books."

        self.assertEqual(result, expected_result)

    def test_rent_book_should_return_error_message_when_title_is_not_registered(self):
        reader_name = 'reader'
        author_name = 'author'
        invalid_title = 'title'
        self.lib.add_reader(reader_name)
        self.lib.add_book(author_name, 'random title')

        result = self.lib.rent_book(reader_name, author_name, invalid_title)
        expected_result = f"""{self.lib.name} Library does not have {author_name}'s "{invalid_title}"."""

        self.assertEqual(result, expected_result)

    def test_rent_book_should_properly_rent_book(self):
        reader_name = 'reader'
        author_name = 'author'
        first_title = 'title1'
        second_title = 'title2'
        self.lib.add_reader(reader_name)
        self.lib.add_book(author_name, first_title)
        self.lib.add_book(author_name, second_title)

        self.lib.rent_book(reader_name, author_name, first_title)

        self.assertEqual([{author_name: first_title}], self.lib.readers[reader_name])
        self.assertEqual(1, len(self.lib.books_by_authors[author_name]))
        self.assertTrue(first_title not in self.lib.books_by_authors[author_name])
        self.assertTrue(second_title in self.lib.books_by_authors[author_name])
