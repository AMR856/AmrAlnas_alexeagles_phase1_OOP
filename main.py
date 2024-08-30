from person import Person
from employee import Employee
from customer import Customer
from flight import Flight
from gate import Gate
from airport import Airport
if __name__ == '__main__':
    gate1 = Gate(10, 'Near the biggest plane', 3, (100, 200))
    airport1 = Airport('Amr Alnas\'s Airport',
                    'Alexandria, Egypt',
                    (2004, 1, 1),
                    [gate1],
                    (1000, 2000), True)
    print(airport1.airport_date_of_construction)
    print(airport1.airport_location)
    print(airport1.airport_name)
    print(airport1.airport_size)
    print(airport1.gates)
    print(airport1.wifi_availability)
    print(airport1.not_allowed_items_in_airports)
# print(gate1.gate_allowed_passing_people)
# print(gate1.gate_location)
# print(gate1.gate_number)
# print(gate1.gate_size)
# person1 = Person('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', 'Alexandria, Egypt, Side Bishr')
# print(person1.birthdate)
# print(person1.firstname)
# print(person1.lastname)
# print(person1.address)
# print(person1.email)
# # amira = Person('Amira', 'Ahmed Nbeh', (1999, 4, 1), 'ahnn99992@gmail.com')
# employee1 = Employee('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', '08:30 AM', '5:00 PM', 7000, 'Alexandria Airlines')
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