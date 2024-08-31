import datetime
from models import person
from models import meal
from models.person import Person
from models.employee import Employee
from models.customer import Customer
from models.flight import Flight
from models.gate import Gate
from models.airport import Airport
from models.meal import Meal
from models.movie import Movie
from models.airline import Airline
import uuid
# olive oil, oregano, tomato, olives, mozzarella or other cheese, and many other ingredients
if __name__ == '__main__':
    # gate1 = Gate(10, 'Near the biggest plane', 3, (100, 200))
    movie1 = Movie('The Pursuit of Happyness', 'Gabriele Muccino', 2007, 'Drama', 8.0)
    meal1 = Meal('Pizza', ['olive oil', 'oregano', 'tomato', 'olives', 'mozzarella', 'chesses'], 1250)
    flight_uuid = uuid.uuid4()
    employee1 = Employee('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', '08:30 AM', '5:00 PM', 7000, 'Egyptair')
    print(employee1)
    airline1 = Airline('Egyptair', [employee1], [meal1, movie1])
    dt_departure = datetime.datetime(year=2024, month=9, day=5, hour=7, minute=30)
    dt_arrival = datetime.datetime(year=2024, month=9, day=5, hour=15, minute=30)
    flight1 = Flight(flight_uuid, dt_departure, dt_arrival, 'Alexandria', 'Berlin', 15000, airline1)
    # print(flight1)

# Design and implement a flight booking system that allows users to:

# 1. Choose the most suitable flight based on various parameters like time, price, and airline.
# 2. Select departure and arrival airports.
# 3. Enter customer details during the reservation process.
# 4. Select a meal option and choose from additional services provided by the airline.


# airport1 = Airport('Amr Alnas\'s Airport',
#                 'Alexandria, Egypt',
#                 (2004, 1, 1),
#                 [gate1],
#                 [employee1],
#                 (1000, 2000), True)
# print(airport1)
# person1 = Person('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', 'Alexandria, Egypt, Side Bishr')
# print(person1)
# # amira = Person('Amira', 'Ahmed Nbeh', (1999, 4, 1), 'ahnn99992@gmail.com')
# print(employee1.firstname)
# print(employee1.lastname)
# print(employee1.birthdate)
# print(employee1.email)
# print(employee1.start_hour)
# print(employee1.finish_hour)
# print(employee1.salary)
# print(employee1.airline_name)
# print(employee1.working_hours)
# random_flight = Flight()
# customer1 = Customer('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', 1000, [random_flight])