from CarRegistryExceptions import GarageError
from Car import Car

# Create Garage class and constructor to store the cards in getters and setters below for
# properties / attributes of the garage class


class Garage:

    def __init__(self):
        self._cars = []

    # Creating properties of class
    @property
    def cars(self):
        return self._cars

    @property
    def number_of_cars(self):
        return len(self._cars)

    @property
    def total_value_of_cars(self):
        total_value = 0
        for car in self._cars:
            total_value += car.price
        return total_value

    # Checking if the car is already in the garage by checking the Car object against the garage object
    # If it is not in the garage then it will add it to the list / garage

    def add(self, car):
        if isinstance(car, Car):
            if car in self.cars:
                raise GarageError('This Car is already in the garage')
            self._cars.append(car)

    # Check and remove if the car is in the garage
    def remove(self, car):
        if isinstance(car, Car):
            self._cars.remove(car)

    # Empty out the garage
    def clear(self):
        self._cars.clear()

    def hire_out(self, car):
        if isinstance(car, Car) and car.on_hire == 'TRUE':
            raise GarageError('This car is already on hire')
        car.on_hire = 'TRUE'

    def return_car(self, car):
        if isinstance(car, Car) and car.on_hire == 'FALSE':
            raise GarageError('This car is already in the garage')
        car.on_hire = 'FALSE'
