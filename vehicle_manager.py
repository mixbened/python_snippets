class Vehicle(object):
    def __init__(self, brand, model, kilometers, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service_date = general_service_date

    def edit_kilometers(self, val):
        self.kilometers = val

    def edit_general_service_date(self, val):
        self.general_service_date = val


def show_vehicles(vehicles):
    for item in vehicles:
        print('')
        for vehicle in list(item.__dict__.keys()):
            print(getattr(item, vehicle))

def add_vehicle(vehicles):
    model = input('Set a model: ')
    brand = input('Set a brand: ')
    kilometers = input('Set a kilometers value ')
    general_service_date = input('Set a general Service Date: ')
    new_vehicle = Vehicle(model, brand, kilometers, general_service_date)
    vehicles.append(new_vehicle)
    print('Successfully added the vehicle!')

def save_session(vehicles):
    vehicle_file = open('vehicle.txt', 'w')
    vehicle_dicts = []
    for item in vehicles:
        vehicle_dicts.append(item.__dict__)
    vehicle_file.write(str(vehicle_dicts))
    vehicle_file.close()

def edit_vehicle(vehicles):
    for index, item in enumerate(vehicles):
        print('ID: %d' %index)
        for vehicle in list(item.__dict__.keys()):
            print(getattr(item, vehicle))
    index = input('choose the ID of the Car you want to edit: ')
    selected_vehicle = vehicles[int(index)]
    km = input('What do you want to change? (km/date): ')
    val = input('What do you want to change it to?: ')
    if km == 'km':
        selected_vehicle.kilometers = val
    elif km == 'date':
        selected_vehicle.general_service_date = val
    print('Edit successfull!')


def main():
    print('Hey! This is your vehicle Manager')
    vehicles = []
    while True:
        action = input(
            'What would you like to do? a) show vehicles b) add vehicle c) edit vehicle d) save session(!) - otherwise type exit)')
        if action == 'a':
            show_vehicles(vehicles)
        elif action == 'b':
            add_vehicle(vehicles)
        elif action == 'c':
            edit_vehicle(vehicles)
        elif action == 'd':
            save_session(vehicles)
        keep = input('Want to keep going? (y/n): ')
        if keep == 'n':
            break

if __name__ == '__main__':
    main()