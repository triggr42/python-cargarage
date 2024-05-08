import unittest
from Car import Car
from CarRegistry import Garage

# Creating Car Registry Unit Tests


class CarRegistryTests(unittest.TestCase):

    def setUp(self):
        # set up so the garage is populated / not changed on each run - saves repetition through the tests
        self._garage = Garage()

    def test_create_garage_with_6_cars(self):

        car1 = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAA')
        car2 = Car('BMW', 'M3', 3, 4000, 0, 25000, 'OW55 AAB')
        car3 = Car('BMW', 'M4', 3, 4000, 2, 35000, 'OW55 AAC')
        car4 = Car('BMW', 'M5', 5, 5800, 10, 35000, 'OW55 AAD')
        car5 = Car('Audi', 'RS6', 5, 4800, 0, 60000, 'OW55 AAE')
        car6 = Car('Audi', 'RS3', 3, 4800, 0, 45000, 'OW55 AAF')

        self._garage.add(car1)
        self._garage.add(car2)
        self._garage.add(car3)
        self._garage.add(car4)
        self._garage.add(car5)
        self._garage.add(car6)

        self.assertEqual(6, self._garage.number_of_cars)
        self.assertEqual(225000, self._garage.total_value_of_cars)

    def test_add_existing_car_to_garage_SameObject(self):

        car1 = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAA')
        car2 = Car('BMW', 'M3', 3, 4000, 0, 25000, 'OW55 AAB')
        car3 = Car('BMW', 'M4', 3, 4000, 2, 35000, 'OW55 AAC')
        car4 = Car('BMW', 'M5', 5, 5800, 10, 35000, 'OW55 AAD')
        car5 = Car('Audi', 'RS6', 5, 4800, 0, 60000, 'OW55 AAE')
        car6 = Car('Audi', 'RS3', 3, 4800, 0, 45000, 'OW55 AAF')

        self._garage.add(car1)
        self._garage.add(car2)
        self._garage.add(car3)
        self._garage.add(car4)
        self._garage.add(car5)
        self._garage.add(car6)

        self._garage.add(car1)

        self.assertEqual(6, self._garage.number_of_cars)
        self.assertEqual(225000, self._garage.total_value_of_cars)

    def test_add_existing_car_to_garage_DiffObject(self):

        car1 = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAA')
        car2 = Car('BMW', 'M3', 3, 4000, 0, 25000, 'OW55 AAB')
        car3 = Car('BMW', 'M4', 3, 4000, 2, 35000, 'OW55 AAC')
        car4 = Car('BMW', 'M5', 5, 5800, 10, 35000, 'OW55 AAD')
        car5 = Car('Audi', 'RS6', 5, 4800, 0, 60000, 'OW55 AAE')
        car6 = Car('Audi', 'RS3', 3, 4800, 0, 45000, 'OW55 AAF')

        self._garage.add(car1)
        self._garage.add(car2)
        self._garage.add(car3)
        self._garage.add(car4)
        self._garage.add(car5)
        self._garage.add(car6)

        # Creating a new car that has a different licence so that the same / diff object check can differ
        # using the EQ method in Car class

        cary = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAG')
        self._garage.add(cary)

        self.assertEqual(7, self._garage.number_of_cars)
        self.assertEqual(250000, self._garage.total_value_of_cars)

    def test_remove_existing_car_from_garage(self):
        car1 = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAA')
        car2 = Car('BMW', 'M3', 3, 4000, 0, 25000, 'OW55 AAB')
        car3 = Car('BMW', 'M4', 3, 4000, 2, 35000, 'OW55 AAC')
        car4 = Car('BMW', 'M5', 5, 5800, 10, 35000, 'OW55 AAD')
        car5 = Car('Audi', 'RS6', 5, 4800, 0, 60000, 'OW55 AAE')
        car6 = Car('Audi', 'RS3', 3, 4800, 0, 45000, 'OW55 AAF')

        self._garage.add(car1)
        self._garage.add(car2)
        self._garage.add(car3)
        self._garage.add(car4)
        self._garage.add(car5)
        self._garage.add(car6)

        self._garage.remove(car1)

        self.assertEqual(5, self._garage.number_of_cars)
        self.assertEqual(200000, self._garage.total_value_of_cars)

    def test_remove_non_exist_car_from_garage(self):
        car1 = Car('BMW', 'M2', 3, 4000, 0, 25000, 'OW55 AAA')
        car2 = Car('BMW', 'M3', 3, 4000, 0, 25000, 'OW55 AAB')
        car3 = Car('BMW', 'M4', 3, 4000, 2, 35000, 'OW55 AAC')
        car4 = Car('BMW', 'M5', 5, 5800, 10, 35000, 'OW55 AAD')
        car5 = Car('Audi', 'RS6', 5, 4800, 0, 60000, 'OW55 AAE')
        car6 = Car('Audi', 'RS3', 3, 4800, 0, 45000, 'OW55 AAF')

        self._garage.add(car1)
        self._garage.add(car2)
        self._garage.add(car3)
        self._garage.add(car4)
        self._garage.add(car6)

        self._garage.remove(car5)

        self.assertEqual(5, self._garage.number_of_cars)
        self.assertEqual(165000, self._garage.total_value_of_cars)
