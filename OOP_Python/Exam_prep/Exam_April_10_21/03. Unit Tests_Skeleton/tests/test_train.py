from unittest import TestCase
from project.train.train import Train


class TrainTest(TestCase):

    def setUp(self) -> None:
        self.train = Train('TestName', 3)

    def test_train_innit(self):
        name = 'Train'
        capacity = 3
        train = Train(name, capacity)

        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)

    def test_adds_passenger_and_returns_proper_string(self):
        passenger_name = 'Pesho'
        result = self.train.add(passenger_name)

        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_add_raises_when_capacity_is_reached(self):
        self.train.passengers = ['Pesho', 'Gosho', 'Ivan']

        with self.assertRaises(ValueError) as error:
            self.train.add('Dragan')
        self.assertEqual("Train is full", str(error.exception))

    def test_add_raises_when_passenger_already_exists(self):
        passenger_name = 'Pesho'
        self.train.passengers = [passenger_name]

        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)
        self.assertEqual(f"Passenger {passenger_name} Exists", str(error.exception))

    def test_remove_raises_when_passenger_does_not_exists(self):
        with self.assertRaises(ValueError) as error:
            self.train.remove('Pesho')
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_passenger_successfully(self):
        passenger_name = 'Pesho'
        self.train.passengers = [passenger_name, 'Ivan']
        result = self.train.remove(passenger_name)
        self.assertEqual(f"Removed {passenger_name}", result)
        self.assertTrue(passenger_name not in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))
        self.assertTrue('Ivan' in self.train.passengers)
