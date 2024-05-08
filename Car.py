from CarExceptions import *
import re


class Car:

    # Define Class Constants
    MIN_SEAT_CAPACITY = 1
    MAX_SEAT_CAPACITY = 10
    MIN_MPG = 0
    MIN_WIDTH = 1000
    MAX_WIDTH = 2500
    MIN_LENGTH = 1000
    MAX_LENGTH = 10000
    MIN_CAR_ID = 1
    VALID_MAKE = ['CHEVROLET', 'CHRYSLER', 'FORD', 'HONDA', 'ISUZU', 'TOYOTA']
    MAX_CAR_SPEED = 305

    largest_car_id = 0

    # Initialising constructor
    def __init__(self, car_id=1, licence='OY55 ABC', make='Honda', model='Civic', sipp_code='FDAR', seat_capacity=1,
                 width=1000, length=1000, maximum_speed=100.55, mpg=25.00, on_hire=False):

        self.car_id = car_id
        self.licence = licence
        self.make = make
        self.model = model
        self.sipp_code = sipp_code
        self.seat_capacity = seat_capacity
        self.width = width
        self.length = length
        self.maximum_speed = maximum_speed
        self.mpg = mpg
        self.on_hire = on_hire
        Car.largest_car_id = (int(car_id)+1)

    def __str__(self):
        # Set vowels for all cases
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        # Decider for outputting a or an in the sentence
        a_or_an = ''
        if len(self.make) > 0 and self.make.startswith(vowels):
            a_or_an = 'n'
        # Output the car details using f to include the object in the string
        return f'{self.car_id},{self.licence},{self.make},{self.model},{self.sipp_code},{self.seat_capacity},' \
               f'{self.width},{self.length},{self.maximum_speed},{self.mpg},{self.on_hire} \n'

    # Creating a method so that we can check if the cars are the same but different based on their licence
    # plate but also using this method to check if we are referencing the same car or a different car with same
    # attributes
    def __eq__(self, other):
        if self.licence == other.licence:
            return True
        return False

    # Getters and setters methods for property of car and blank instances output
    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        if car_id == '':
            raise CarCarIdError('Car ID should not be blank')
        elif int(car_id) < Car.MIN_CAR_ID:
            raise CarCarIdError('Car ID should not be less than 1')
        self._car_id = car_id

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if make.upper() not in Car.VALID_MAKE:
            raise CarMakeError('Car should have a valid make')
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if model == '':
            raise CarModelError('Car must have a model')
        self._model = model

    @property
    def sipp_code(self):
        return self._sipp_code

    # Check that the doors are between the minimum and maximum set
    @sipp_code.setter
    def sipp_code(self, sipp_code):
        if not (
                re.match(
                    r'(^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$)', sipp_code)):
            raise CarSippCodeError('The SIPP code must be in the correct format - see here for more information'
                                   ' https://car-hire-centre.co.uk/sipp-codes.html')
        self._sipp_code = sipp_code

    @property
    def seat_capacity(self):
        return self._seat_capacity

    @seat_capacity.setter
    def seat_capacity(self, seat_capacity):
        if not int(seat_capacity) % 1 == 0 or not (Car.MIN_SEAT_CAPACITY <= int(seat_capacity) <= Car.MAX_SEAT_CAPACITY):
            raise CarSeatCapacityError(f'Seat capacity should be a number between {Car.MIN_SEAT_CAPACITY} and'
                                       f' {Car.MAX_SEAT_CAPACITY}')
        self._seat_capacity = seat_capacity

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not (Car.MIN_WIDTH <= int(width) <= Car.MAX_WIDTH):
            raise CarWidthError(f'width must be between {Car.MIN_WIDTH} and {Car.MAX_WIDTH}')
        self._width = width

    @property
    def licence(self):
        return self._licence

    @licence.setter
    def licence(self, licence):
        if not (
                re.match(
                    r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|'
                    r'(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|'
                    r'(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{3}$)', licence)):
            raise CarLicenceError('The car must have a licence plate in the format AA12 AAA')
        self._licence = licence

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if not (Car.MIN_LENGTH <= int(length) <= Car.MAX_LENGTH):
            raise CarLengthError(f'length must be between {Car.MIN_LENGTH} and {Car.MAX_LENGTH}')
        self._length = length

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, maximum_speed):
        if not (float(maximum_speed) <= Car.MAX_CAR_SPEED):
            raise CarMaxSpeedError(f'Max speed must be less than or equal to {Car.MAX_CAR_SPEED}')
        self._maximum_speed = maximum_speed

    @property
    def mpg(self):
        return self._mpg

    @mpg.setter
    def mpg(self, mpg):
        if not (float(mpg) >= Car.MIN_MPG):
            raise CarMinMpgError(f'Min car MPG must be greater than {Car.MIN_MPG}')
        self._mpg = mpg

    @property
    def on_hire(self):
        return self._on_hire

    @on_hire.setter
    def on_hire(self, on_hire):
        if on_hire == '':
            raise CarOnHireError('Car on hire should not be blank')
        if on_hire.upper() != 'FALSE' and on_hire != 'TRUE':
            raise CarOnHireError('On hire must be True or False')
        self._on_hire = on_hire

