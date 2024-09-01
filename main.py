import uuid
import datetime
from models.person import Person
from models.meal import Meal
from models.movie import Movie
from models.flight import Flight
from models.employee import Employee
from models.customer import Customer
from models.airport import Airport
from models.gate import Gate
from models.airline import Airline

if __name__ == '__main__':
    airline1 = Airline('FlyEgypt', None, None, None)
    print(airline1.to_dict())
    # person = Person('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com')
    # print(person.to_dict())
    # employee1 = Employee('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', '9:00 AM', '6:00 PM', 8000, 'FlyEgypt')
    # print(employee1.to_dict())
    # gate1 = Gate(1, 'Near the back of the airport', 15, (100, 200))
    # print(gate1.to_dict())
    # customer1 = Customer('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', 10000, None)
    # print(customer1.to_dict())
    # meal1 = Meal('Eggs', ['Eggs', 'Butter', 'Black pepper', 'Yogurt'], 250)
    # print(meal1.to_dict())
    # employee2 = Employee('Amira', 'Ahmed', (1999, 4, 1), 'amira@gmail.com', '8:00 AM', '5:00 PM', 8000, 'Petroleum Air Services')
    # dt_departure = datetime.datetime(year=2024, month=9, day=5, hour=7, minute=30)
    # dt_arrival = datetime.datetime(year=2024, month=9, day=5, hour=15, minute=30)
    # movie1 = Movie('The Pursuit of Happyness', 'Gabriele Muccino', 2007, 'Drama', 8.0)
    # print(movie1.to_dict())
    # flight1 = Flight(dt_departure, dt_arrival, 'Alexanrdia', 'Berlin', 9000)
    # print(flight1.to_dict())
    # airport1 = Airport("Amr's Airport", 'Alexandria, Egypt', (2004, 1, 1), [gate1], [employee1, employee2], (1000, 2000), True)
    # print(airport1.to_dict())
    # airline1.add_employee(employee1)
    # airline1.add_employee(employee2) 
    # airline1.add_service(meal1)
    # airline1.add_service(movie1)
    # print(flight1.__dict__)
    # print(customer1)
    pass
