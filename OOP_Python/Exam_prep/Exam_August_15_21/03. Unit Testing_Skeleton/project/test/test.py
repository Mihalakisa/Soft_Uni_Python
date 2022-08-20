from unittest import TestCase
from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Test Shop')

    def test_innit(self):
        self.assertEqual('Test Shop', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_raise_error_when_quantity_is_less_or_equal_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food('Pesho', -4)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food('Pesho', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_good_case(self):
        food_name = 'Wiskas'
        grams = 100
        string_text = f"Successfully added {grams:.2f} grams of {food_name}."
        result = self.pet_shop.add_food(food_name, grams)
        self.assertEqual(string_text, result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(grams, self.pet_shop.food[food_name])

    def test_add_food_adds_food_qty_to_existing_food(self):
        food_name = 'Wiskas'
        initial_qty = 100
        self.pet_shop.food[food_name] = initial_qty

        add_qty = 50
        result = self.pet_shop.add_food(food_name, add_qty)

        self.assertEqual(f"Successfully added {add_qty:.2f} grams of {food_name}.", result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(initial_qty + add_qty, self.pet_shop.food[food_name])

    def test_add_pet_raise_error_when_name_is_the_same(self):
        pet_name1 = 'Spark'
        pet_name2 = 'Spark'
        self.pet_shop.pets.append(pet_name1)

        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet(pet_name2)
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_add_pet_good_case(self):
        pet_name1 = 'Spark'
        pet_name2 = 'Bark'
        expected_result = f"Successfully added {pet_name1}."
        result = self.pet_shop.add_pet(pet_name1)
        self.assertEqual(result, expected_result)
        self.assertTrue(pet_name1 in self.pet_shop.pets)
        self.pet_shop.add_pet(pet_name2)
        self.assertEqual(2, len(self.pet_shop.pets))

    def test_feed_pet_error_when_name_not_in_pets(self):
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet('food_name', 'pet_name')

        self.assertEqual("Please insert a valid pet name", str(error.exception))

    def test_feed_pet_error_when_food_not_in_foods(self):
        pet_name = 'Spark'
        self.pet_shop.pets.append(pet_name)

        result = self.pet_shop.feed_pet('invalid_food', pet_name)
        self.assertEqual(f'You do not have invalid_food', result)

    def test_feed_pet_adding_food_quantity(self):
        food_name = 'Wiskas'
        pet_name = 'Spark'
        initial_qty = 65

        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = initial_qty
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual(initial_qty + 1000, self.pet_shop.food[food_name])

    def test_feed_pet_when_successfully_fed(self):
        pet_name = 'Spark'
        food_name = 'Wiskas'
        initial_qty = 165
        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = initial_qty
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(initial_qty - 100, self.pet_shop.food[food_name])

    def test_repr(self):
        pet_name = 'Spark'
        self.pet_shop.add_pet(pet_name)
        self.assertEqual(repr(self.pet_shop), f'Shop {self.pet_shop.name}:\nPets: '
                                                           f'{", ".join(self.pet_shop.pets)}')