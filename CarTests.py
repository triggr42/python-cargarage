# Importing Unit test module and Car object from car py
import unittest
from Car import Car
from CarExceptions import CarMakeError
from CarExceptions import CarModelError
from CarExceptions import CarNumberOfDoorsError
from CarExceptions import CarEngineSizeError
from CarExceptions import CarAgeError
from CarExceptions import CarPriceError
from CarExceptions import CarLicenceError


# Create Car class unit test using the arrange act assert framework / layout


class CarTests(unittest.TestCase):

    def test_create_car_okay(self):

        car = Car('BMW', 'M3', 3, 4000, 12, 30000, 'AY06 HIL')

        self.assertEqual('BMW', car.make)
        self.assertEqual('M3', car.model)
        self.assertEqual(3, car.number_of_doors)
        self.assertEqual(4000, car.engine_size)
        self.assertEqual(12, car.age)
        self.assertEqual(30000, car.price)
        self.assertEqual('AY06 HIL', car.licence)
        self.assertEqual('I am a BMW M3 and the licence number is AY06 HIL', str(car))
    # Test the default car when there are no entries

    def test_create_assumed_car(self):

        car = Car()

        self.assertEqual('Honda', car.make)
        self.assertEqual('Civic', car.model)
        self.assertEqual(0, car.number_of_doors)
        self.assertEqual(2000, car.engine_size)
        self.assertEqual(15, car.age)
        self.assertEqual(5000, car.price)
        self.assertEqual('OY55 ABC', car.licence)
        self.assertEqual('I am a Honda Civic and the licence number is OY55 ABC', str(car))

    # Test the class when there is the engine size is below 0
    # Assert raises exceptions and check that the correct message is coming out in the correct context
    # For the below exceptions
    def test_create_car_impossible_engine_size(self):

        with self.assertRaises(CarEngineSizeError) as context:
            car = Car('BMW', 'M3', 3, -3000, 12, 30000, 'AY06 HIL')

        self.assertEqual(f'Engine size must be between {Car.MIN_ENGINE_SIZE} and {Car.MAX_ENGINE_SIZE}',
                         str(context.exception))

    def test_create_car_impossible_engine_size2(self):

        with self.assertRaises(CarEngineSizeError) as context:
            car = Car('BMW', 'M3', 3, 12000, 12, 30000, 'AY06 HIL')

        self.assertEqual(f'Engine size must be between {Car.MIN_ENGINE_SIZE} and {Car.MAX_ENGINE_SIZE}',
                         str(context.exception))

    def test_create_car_missing_make(self):

        with self.assertRaises(CarMakeError) as context:
            car = Car('', 'M3', 3, 4000, 12, 30000, 'AY06 HIL')

        self.assertEqual('Car should have a make', str(context.exception))

    def test_create_car_missing_model(self):

        with self.assertRaises(CarModelError) as context:
            car = Car('BMW', '', 3, 4000, 12, 30000, 'AY06 HIL')

        self.assertEqual('Car must have a model', str(context.exception))

    def test_create_car_doors_too_low(self):

        with self.assertRaises(CarNumberOfDoorsError) as context:
            car = Car('BMW', 'M3', -2, 4000, 12, 30000, 'AY06 HIL')

        self.assertEqual(f'Number of doors must be between {Car.MIN_NUMBER_OF_DOORS} and '
                         f'{Car.MAX_NUMBER_OF_DOORS}', str(context.exception))

    def test_create_car_doors_to_high(self):

        with self.assertRaises(CarNumberOfDoorsError) as context:
            car = Car('BMW', 'M3', 20, 4000, 12, 30000, 'AY06 HIL')

        self.assertEqual(f'Number of doors must be between {Car.MIN_NUMBER_OF_DOORS} and '
                         f'{Car.MAX_NUMBER_OF_DOORS}', str(context.exception))

    def test_create_car_age_too_low(self):

        with self.assertRaises(CarAgeError) as context:
            car = Car('BMW', 'M3', 3, 4000, -3, 30000, 'AY06 HIL')

        self.assertEqual(f'age must be between {Car.MIN_AGE} and {Car.MAX_AGE}', str(context.exception))

    def test_create_car_age_too_high(self):

        with self.assertRaises(CarAgeError) as context:
            car = Car('BMW', 'M3', 3, 4000, 180, 30000, 'AY06 HIL')

        self.assertEqual(f'age must be between {Car.MIN_AGE} and {Car.MAX_AGE}', str(context.exception))

    def test_create_car_price_too_low(self):

        with self.assertRaises(CarPriceError) as context:
            car = Car('BMW', 'M3', 3, 4000, 12, -200000, 'AY06 HIL')

        self.assertEqual(f'price must be between {Car.MIN_PRICE} and {Car.MAX_PRICE}', str(context.exception))

    def test_create_car_price_too_high(self):

        with self.assertRaises(CarPriceError) as context:
            car = Car('BMW', 'M3', 3, 4000, 12, 200000, 'AY06 HIL')

        self.assertEqual(f'price must be between {Car.MIN_PRICE} and {Car.MAX_PRICE}', str(context.exception))

    def test_create_car_licence_blank(self):

        with self.assertRaises(CarLicenceError) as context:
            car = Car('BMW', 'M3', 3, 4000, 12, 30000, '')

        self.assertEqual('The car must have a licence plate', str(context.exception))

    def test_create_car_manufacture_age_invalid_date_format(self):

        with self.assertRaises(CarAgeError) as context:
            car = Car('BMW', 'M3', 3, 4000, 12, 30000, 'AY06 HIL', 'O5/05/2020')

        self.assertEqual('Date of Manufacture must be in YYYY/MM/DD format', str(context.exception))


