from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def test_mammal_init_should_create_proper_obj(self):
        name = 'Pesho'
        mammal_type = 'Mammal_Type'
        sound = 'sound'
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_result(self):
        name = 'Pesho'
        mammal_type = 'Mammal_Type'
        sound = 'sound'
        mammal = Mammal(name, mammal_type, sound)

        actual_result = mammal.make_sound()
        expected_result = f"{name} makes {sound}"

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_returns_animals(self):
        mammal = Mammal("Name", "Type", "Sound")

        actual_result = mammal.get_kingdom()
        expected_result = "animals"

        self.assertEqual(expected_result, actual_result)

    def test_info_returns_proper_string(self):
        mammal = Mammal("Name", "Type", "Sound")

        actual_result = mammal.info()
        expected_result = f"{mammal.name} is of type {mammal.type}"

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
