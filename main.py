
from models.person import Person


if __name__ == '__main__':
    # airline1 = Airline('FlyEgypt', None, None)
    person = Person('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com')
    print(person.to_dict())
    # employee1 = Employee('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', '9:00 AM', '6:00 PM', 8000, 'FlyEgypt')
    # print(employee1.employee_id)
    pass
    # gate1 = Gate(1, 'Near the back of the airport', 15, (100, 200))
    # customer1 = Customer('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', 10000, None)
    # meal1 = Meal('Eggs', ['Eggs', 'Butter', 'Black pepper', 'Yogurt'], 250)
    # employee2 = Employee('Amira', 'Ahmed', (1999, 4, 1), 'amira@gmail.com', '8:00 AM', '5:00 PM', 8000, 'Petroleum Air Services')
    # dt_departure = datetime.datetime(year=2024, month=9, day=5, hour=7, minute=30)
    # dt_arrival = datetime.datetime(year=2024, month=9, day=5, hour=15, minute=30)
    # movie1 = Movie('The Pursuit of Happyness', 'Gabriele Muccino', 2007, 'Drama', 8.0)
    # flight1 = Flight(uuid.uuid4(), dt_departure, dt_arrival, 'Alexanrdia', 'Berlin', 10000)

    # airport1 = Airport("Amr's Airport", 'Alexandria, Egypt', (2004, 1, 1), [gate1], [employee1, employee2], (1000, 2000), True)
    # airline1.add_employee(employee1)
    # airline1.add_employee(employee2)
    # airline1.add_service(meal1)
    # airline1.add_service(movie1)
    # print(flight1.__dict__)
    # print(customer1)
