class DataAccess:

    CAR_FILE = r'C:\temp\CarRegistry.dat'

    def read_all(self):
        list_of_car_strings = []
        with open(self.CAR_FILE, 'r') as file:
            for line in file:
                list_of_car_strings.append(line[:-1])
        return list_of_car_strings

    def write_all(self, write_data):
        with open(self.CAR_FILE, 'w') as file:
            file.writelines(write_data)
