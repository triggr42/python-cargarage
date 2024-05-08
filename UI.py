from Car import Car
from CarRegistry import Garage
from CarRegistryExceptions import GarageError
from CarExceptions import *
from DataAccess import DataAccess


class UI:
    END_OF_ADD_STRING = "can't be blank (or Q to return to the main menu)\n"

    def __init__(self):
        self._garage = Garage()
        self._data_access = DataAccess()

    def read_data_store(self):
        all_cars_as_list_of_strings = self._data_access.read_all()

        for car_string in all_cars_as_list_of_strings:
            split_string = car_string.split(",")
            car = Car(car_id=split_string[0], licence=split_string[1], make=split_string[2], model=split_string[3]
                      , sipp_code=split_string[4], seat_capacity=int(split_string[5]), width=int(split_string[6])
                      , length=int(split_string[7]), maximum_speed=float(split_string[8]), mpg=float(split_string[9])
                      , on_hire=split_string[10].upper())
            try:
                self._garage.add(car)
            except GarageError as e:
                print(f'{str(e)}')

    def write_data_store(self):

        list_of_cars_as_strings = []

        for car in self._garage.cars:
            list_of_cars_as_strings.append(str(car))
        self._data_access.write_all(''.join(list_of_cars_as_strings))

    # Create a looping count of the cars for identification
    def display_garage_contents(self):
        if self._garage.number_of_cars == 0:
            return

        print(f'{"POS":>4} {"ID":>2} {"Reg":>2} {"Manufacturer":>20} {"Model":>8} {"SIPP":>10}'
                  f'{"Seats":>8} {"Width":>8} {"Length":>8} {"Spd":>7} {"MPG":>6} {"OnHire":>10}')
        for count, car in enumerate(self._garage.cars):
            print(f'{count+1:>3} {car.car_id:>3} {car.licence:<11} {car.make:<15} {car.model:<11} {car.sipp_code:>1}'
                  f'{car.seat_capacity:>8} {car.width:>8} {car.length:>8} {car.maximum_speed:>6} {car.mpg:>7} '
                  f'{car.on_hire:>10}')

    # Display the menu options related to a key to press for the option
    def display_menu_options(self):
        print('Menu')
        print('A - Add car to the garage')
        print('D - Remove car from the garage')
        print('H - Hire a car from the garage')
        print('R - Return a car to the garage')
        print('U - Update garage')
        print('X - Quit Carnucopia application')


    # Menu choice valid choices and pass if none
    def get_menu_choice(self):
        characters = {'a', 'A', 'd', 'D', 'h', 'H', 'r', 'R', 'q', 'q', 'Q'}
        value = input()
        while not any(characters in characters for characters in value) and len(value) != 1:
            pass
        return value

    # add car function with error
    def add_car(self):
        car = self.get_car_details()
        try:
            self._garage.add(car)
        except GarageError as e:
            print(f'{str(e)}')

        # Get the details of the car and check for quit menu option at each step if okay then carry on else exception
    def get_car_details(self):

        make = ''
        model = ''
        licence = ''
        sipp_code = ''
        seat_capacity = ''
        width = ''
        length = ''
        maximum_speed = ''
        mpg = ''

        # Add in trys throughout the UI so that if Q is pressed and details blank then the application quits as
        # per spec
        while True:
            # Conditions for while true try catch
            try:
                while make == '':
                    make = input(f'Enter the car make. {UI.END_OF_ADD_STRING}').upper()
                    if make.upper() == 'Q':
                        return
                while model == '':
                    model = input(f'Enter the car model. {UI.END_OF_ADD_STRING}').upper()
                    if model.upper() == 'Q':
                        return
                while licence == '':
                    licence = input(f'Enter the car licence plate. {UI.END_OF_ADD_STRING}').upper()
                    if licence.upper() == 'Q':
                        return
                while sipp_code == '':
                    sipp_code = input(f'Enter the SIPP code. Format AAAA {UI.END_OF_ADD_STRING}').upper()
                    if sipp_code.upper() == 'Q':
                        return
                while seat_capacity == '':
                    seat_capacity = input(f'Enter the seat capacity. {UI.END_OF_ADD_STRING}')
                    if seat_capacity.upper() == 'Q':
                        return
                    try:
                        seat_capacity = int(seat_capacity)
                    except ValueError:
                        print('Input must be Q or an integer')
                        seat_capacity = ''
                while width == '':
                    width = input(f'Enter the width. {UI.END_OF_ADD_STRING}').upper()
                    if width.upper() == 'Q':
                        return
                    try:
                        width = int(width)
                    except ValueError:
                        print('Input must be Q or an integer')
                        width = ''
                while length == '':
                    length = input(f'Enter the length. {UI.END_OF_ADD_STRING}')
                    if length.upper() == 'Q':
                        return
                    try:
                        length = int(length)
                    except ValueError:
                        print('Input must be Q or an integer')
                        length = ''
                while maximum_speed == '':
                    maximum_speed = input(f'Enter the maximum speed. {UI.END_OF_ADD_STRING}')
                    if maximum_speed.upper() == 'Q':
                        return
                    try:
                        maximum_speed = int(maximum_speed)
                    except ValueError:
                        print('Input must be Q or a decimal')
                        maximum_speed = ''
                while mpg == '':
                    mpg = input(f'Enter the mpg. {UI.END_OF_ADD_STRING}')
                    if mpg.upper() == 'Q':
                        return
                    try:
                        mpg = int(mpg)
                    except ValueError:
                        print('Input must be Q or a decimal')
                        mpg = ''

                # Assign object details
                car = Car(car_id=Car.largest_car_id, make=make, model=model, licence=licence, sipp_code=sipp_code,
                          seat_capacity=seat_capacity, width=width, length=length, maximum_speed=maximum_speed,
                          mpg=mpg, on_hire='FALSE')
                return car

            except CarMakeError as e:
                print(f'{str(e)}')
                make = ''

            except CarModelError as e:
                print(f'{str(e)}')
                model = ''

            except CarLicenceError as e:
                print(f'{str(e)}')
                licence = ''

            except CarSippCodeError as e:
                print(f'{str(e)}')
                sipp_code = ''

            except CarSeatCapacityError as e:
                print(f'{str(e)}')
                seat_capacity = ''

            except CarWidthError as e:
                print(f'{str(e)}')
                width = ''

            except CarLengthError as e:
                print(f'{str(e)}')
                length = ''

            except CarMaxSpeedError as e:
                print(f'{str(e)}')
                maximum_speed = ''

            except CarMinMpgError as e:
                print(f'{str(e)}')
                mpg = ''

    # Remove the car error
    def remove_car(self):
        if self._garage.number_of_cars > 0:
            try:
                car = self.select_car('remove')
                self._garage.remove(car)
            except GarageError as e:
                print(f'{str(e)}')


    def hire_out(self):
        if self._garage.number_of_cars > 0:
            try:
                car = self.select_car('hire out')
                self._garage.hire_out(car)
            except GarageError as e:
                print(f'{str(e)}')

    def return_car(self):
        if self._garage.number_of_cars > 0:
            try:
                car = self.select_car('return to the garage')
                self._garage.return_car(car)
            except GarageError as e:
                print(f'{str(e)}')

    # Select the car and change its position
    def select_car(self, operation):
        pos = self.get_car_pos(f'Which car would you like to {operation} from the Garage '
                               f'(please enter the POS number)?\n');
        car = self._garage.cars[pos-1]
        return car

    def get_car_pos(self, message):
        while True:
            try:
                pos = input(message)
                while not pos.isnumeric or int(pos) <= 0 or int(pos) > self._garage.number_of_cars:
                    print(f'Invalid POS. Must lie between 1 and {self._garage.number_of_cars}')
                    pos = input(message)
                return int(pos)
            except ValueError:
                print('Input must be an integer')


