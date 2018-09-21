class Vehicle(object):
    def __init__(self, brand, model, kilometers, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service_date = general_service_date

    def edit_kilometers(self):


def main():
    print('Hey! This is your vehicle Manager')
    action = input('What would you like to do?')
    