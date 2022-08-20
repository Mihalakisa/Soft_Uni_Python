from unittest import TestCase
from project.plantation import Plantation


class PlantationTests(TestCase):
    SIZE = 1

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_raises_value_error_negative(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -4
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_append_name_wen_does_not_exist(self):
        self.pl = Plantation(2)
        result = self.pl.hire_worker('Pesho')
        self.assertEqual(len(self.pl.workers), 1)
        self.assertEqual(f"Pesho successfully hired.", result)

    def test_hire_worker_append_name_wen_does_already_exist(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Pesho')
        with self.assertRaises(ValueError) as error:
            self.pl.hire_worker('Pesho')
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_planing_if_worker_not_in_workers_error_msg(self):
        name = 'Pesho'
        self.plantation.workers = ['Ivan']

        with self.assertRaises(ValueError) as error:
            self.plantation.planting(name, 'carrot')

        self.assertEqual(f"Worker with name {name} is not hired!", str(error.exception))

    def test_planing_when_plantation_is_full_error(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Ivan')
        self.pl.planting('Ivan', 'carrots')

        with self.assertRaises(ValueError) as error:
            self.pl.planting('Ivan', 'tomatoes')

        self.assertEqual("The plantation is full!", str(error.exception))

    def test_planting_first_plant(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Ivan')
        self.assertEqual(f"Ivan planted it's first Rose.", self.pl.planting('Ivan', 'Rose'))

    def test_planing_more_plants(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Ivan')
        self.pl.planting('Ivan', 'Rose')
        self.assertEqual(f"Ivan planted Rose.", self.pl.planting('Ivan', 'Rose'))

    def test_str_wrong_output(self):
        self.assertEqual(Plantation(2).__str__().strip(), "Plantation size: 2")
        self.pl = Plantation(2)
        self.pl.hire_worker('Ivan')
        self.pl.planting('Ivan', 'Rose')
        self.assertEqual(self.pl.__str__().strip(), "Plantation size: 2\nIvan\nIvan planted: Rose")

    def test_repr_wrong_output(self):
        self.assertEqual(Plantation(2).__repr__().strip(), "Size: 2\nWorkers:")
        self.pl = Plantation(2)
        self.pl.hire_worker('Ivan')
        self.pl.planting('Ivan', 'Rose')
        self.assertEqual(self.pl.__repr__().strip(), "Size: 2\nWorkers: Ivan")

    def test_len_wrong_count(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Ivan')
        self.pl.plants['Ivan'] = ['Rose']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Ivan')
        self.pl.hire_worker('Pesho')
        self.pl.plants['Ivan'] = ['Rose']
        self.pl.plants['Pesho'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    def test_planting_wrong_dict_assigment(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Pesho')
        self.pl.planting('Pesho', "Rose")
        self.pl.planting('Pesho', 'carrots')
        self.assertEqual(len(self.pl.plants['Pesho']), 2)