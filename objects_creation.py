#!/usr/bin/env python3
import datetime
from models.airline import Airline
from models.employee import Employee
from models.customer import Customer
from models.flight import Flight
from models.gate import Gate
from models.airport import Airport
from models.meal import Meal
from models.movie import Movie

def create():
    # Airlines
    airline1 = Airline('Air Arabia Egypt', None, None, None)
    airline2 = Airline('AMC Airlines', None, None, None)
    airline3 = Airline('Nile Air', None, None, None)

    #Airports
    airport1 = Airport("Amr's Alnas", 'Egypt, Alexandria, Borg El Arab', (2010, 2, 15), None, None, (300000, 2000000), True)
    airport2 = Airport("Nile Delta International", 'Egypt, Cairo, Heliopolis', (2005, 6, 30), None, None, (500000, 4000000), True)
    airport3 = Airport("Red Sea Gateway", 'Egypt, Hurghada, Safaga Road', (2012, 11, 20), None, None, (350000, 2500000), True)
    airport4 = Airport("Sphinx Airport", 'Egypt, Giza, Sphinx City', (2018, 7, 5), None, None, (150000, 1200000), True)
    airport5 = Airport("Luxor Valley Airport", 'Egypt, Luxor, Karnak Road', (2008, 4, 18), None, None, (250000, 1800000), True)
    airport6 = Airport("Marsa Alam International", 'Egypt, Marsa Alam, Airport Road', (2003, 9, 25), None, None, (280000, 2200000), True)

    #Customers
    customer1 = Customer('Amira', 'Ahmed Nebh', (1999, 4, 1), 'ahnn99992@gmail.com', 20000, None)
    customer2 = Customer('Omar', 'Hassan Ali', (1987, 7, 15), 'omarhassan87@example.com', 15000, None)
    customer3 = Customer('Sara', 'Mohamed Fathy', (1995, 11, 23), 'sarafathy95@example.com', 22000, None)
    customer4 = Customer('Khaled', 'Youssef ElSayed', (1983, 2, 18), 'khaledys83@example.com', 18000, None)
    customer5 = Customer('Laila', 'Mona Hafez', (2001, 9, 5), 'lailahafez01@example.com', 12000, None)
    customer6 = Customer('Mahmoud', 'Nabil Saleh', (1990, 6, 30), 'mahmoudsaleh90@example.com', 25000, None)
    customer7 = Customer('Nadia', 'Ibrahim Kamel', (1992, 3, 12), 'nadiaik92@example.com', 23000, None)
    customer8 = Customer('Hassan', 'Ahmed Tarek', (1985, 8, 27), 'hassantarek85@example.com', 17000, None)
    customer9 = Customer('Mona', 'Salah Eldin', (1998, 12, 10), 'monasalah98@example.com', 16000, None)
    customer10 = Customer('Youssef', 'Khaled Gamal', (1993, 1, 22), 'youssefgamal93@example.com', 21000, None)
    customer11 = Customer('Fatma', 'Mahmoud Ayman', (2000, 5, 7), 'fatmamay00@example.com', 14000, None)
    customer12 = Customer('Ali', 'Tamer Sayed', (1989, 10, 19), 'alitamer89@example.com', 19000, None)

    # Employees
    employee1 = Employee('Amr', 'Alnas', (2004, 1, 1), 'amer.live477@gmail.com', '7:00 AM', '5:00 PM', 10000, 'Air Arabia Egypt')
    employee2 = Employee('Sara', 'Mahmoud', (2003, 5, 15), 'sara.mahmoud@example.com', '8:00 AM', '6:00 PM', 12000, 'Egyptair')
    employee3 = Employee('Omar', 'Hassan', (2002, 10, 20), 'omar.hassan@example.com', '9:00 AM', '5:00 PM', 11000, 'FlyEgypt')
    employee4 = Employee('Laila', 'Ahmed', (2005, 3, 5), 'laila.ahmed@example.com', '7:30 AM', '4:30 PM', 10500, 'Nile Air')
    employee5 = Employee('Khaled', 'Fathy', (2003, 8, 10), 'khaled.fathy@example.com', '8:30 AM', '6:30 PM', 11500, 'Air Cairo')
    employee6 = Employee('Hana', 'Zaki', (2001, 11, 25), 'hana.zaki@example.com', '7:00 AM', '4:00 PM', 9800, 'EgyptAir')
    employee7 = Employee('Mohamed', 'Ali', (2004, 4, 13), 'mohamed.ali@example.com', '9:00 AM', '5:30 PM', 11300, 'FlyEgypt')
    employee8 = Employee('Noha', 'Khalil', (2002, 7, 30), 'noha.khalil@example.com', '8:00 AM', '4:30 PM', 10700, 'Air Arabia Egypt')
    employee9 = Employee('Youssef', 'Saleh', (2003, 2, 18), 'youssef.saleh@example.com', '7:30 AM', '6:00 PM', 12500, 'Nile Air')
    employee10 = Employee('Fatma', 'Mostafa', (2005, 12, 9), 'fatma.mostafa@example.com', '8:30 AM', '5:30 PM', 10900, 'Air Cairo')

    #Flights
    flight1 = Flight(datetime.datetime(year=2024, month=9, day=5, hour=7, minute=30),
                    datetime.datetime(year=2024, month=9, day=5, hour=15, minute=30),
                    'Alexandria',
                    'Berlin', 9000)
    flight2 = Flight(datetime.datetime(year=2024, month=9, day=6, hour=9, minute=45),
                    datetime.datetime(year=2024, month=9, day=6, hour=17, minute=15),
                    'Cairo',
                    'London', 8500)
    flight3 = Flight(datetime.datetime(year=2024, month=9, day=7, hour=12, minute=0),
                    datetime.datetime(year=2024, month=9, day=7, hour=20, minute=30),
                    'Dubai',
                    'New York', 12000)
    flight4 = Flight(datetime.datetime(year=2024, month=9, day=8, hour=14, minute=15),
                    datetime.datetime(year=2024, month=9, day=8, hour=18, minute=45),
                    'Paris',
                    'Rome', 1100)
    flight5 = Flight(datetime.datetime(year=2024, month=9, day=9, hour=6, minute=30),
                    datetime.datetime(year=2024, month=9, day=9, hour=14, minute=0),
                    'Tokyo',
                    'Sydney', 7800)
    flight6 = Flight(datetime.datetime(year=2024, month=9, day=10, hour=16, minute=0),
                    datetime.datetime(year=2024, month=9, day=10, hour=22, minute=30),
                    'Los Angeles',
                    'Toronto', 3900)
    flight7 = Flight(datetime.datetime(year=2024, month=9, day=11, hour=8, minute=15),
                    datetime.datetime(year=2024, month=9, day=11, hour=16, minute=0),
                    'Mumbai',
                    'Singapore', 4300)
    flight8 = Flight(datetime.datetime(year=2024, month=9, day=12, hour=11, minute=30),
                    datetime.datetime(year=2024, month=9, day=12, hour=19, minute=0),
                    'Hong Kong',
                    'San Francisco', 11300)
    flight9 = Flight(datetime.datetime(year=2024, month=9, day=13, hour=7, minute=0),
                    datetime.datetime(year=2024, month=9, day=13, hour=15, minute=30),
                    'Moscow',
                    'Beijing', 5800)
    flight10 = Flight(datetime.datetime(year=2024, month=9, day=14, hour=10, minute=0),
                    datetime.datetime(year=2024, month=9, day=14, hour=18, minute=30),
                    'Istanbul',
                    'Madrid', 2900)
    flight11 = Flight(datetime.datetime(year=2024, month=9, day=15, hour=13, minute=45),
                    datetime.datetime(year=2024, month=9, day=15, hour=21, minute=15),
                    'Cape Town',
                    'Dubai', 7600)
    flight12 = Flight(datetime.datetime(year=2024, month=9, day=16, hour=15, minute=0),
                    datetime.datetime(year=2024, month=9, day=16, hour=23, minute=45),
                    'Buenos Aires',
                    'Miami', 7100)

    #Gates
    gate1 = Gate(1, 'Besides the fancy Italian Resturant', 20, (70, 50))
    gate2 = Gate(2, 'Near the coffee shop', 15, (60, 45))
    gate3 = Gate(3, 'Opposite the duty-free store', 25, (80, 55))
    gate4 = Gate(4, 'Next to the kids play area', 30, (75, 60))
    gate5 = Gate(5, 'By the entrance of the VIP lounge', 18, (65, 48))
    gate6 = Gate(6, 'Adjacent to the security checkpoint', 22, (72, 52))
    gate7 = Gate(7, 'Close to the information desk', 20, (68, 50))
    gate8 = Gate(8, 'In front of the bookshop', 28, (78, 58))
    gate9 = Gate(9, 'Next to the souvenir store', 24, (73, 53))

    #Meals
    meal1 = Meal('Sushi', ['Rice', 'Nori', 'Fish', 'Vegetables'], 700)
    meal2 = Meal('Spaghetti Bolognese', ['Spaghetti', 'Ground Beef', 'Tomato Sauce', 'Onion', 'Garlic'], 850)
    meal3 = Meal('Caesar Salad', ['Romaine Lettuce', 'Croutons', 'Parmesan Cheese', 'Caesar Dressing', 'Chicken'], 450)
    meal4 = Meal('Tacos', ['Tortillas', 'Ground Beef', 'Cheese', 'Lettuce', 'Tomato', 'Sour Cream'], 600)
    meal5 = Meal('Chicken Curry', ['Chicken', 'Curry Sauce', 'Rice', 'Coconut Milk', 'Spices'], 900)
    meal6 = Meal('Vegetable Stir-Fry', ['Broccoli', 'Carrots', 'Bell Peppers', 'Soy Sauce', 'Tofu'], 500)

    # Movies
    movie1 = Movie('The Pursuit of Happyness', 'Gabriele Muccino', 2007, 'Drama', 8.0)
    movie2 = Movie('Inception', 'Christopher Nolan', 2010, 'Sci-Fi', 8.8)
    movie3 = Movie('The Shawshank Redemption', 'Frank Darabont', 1994, 'Drama', 9.3)
    movie4 = Movie('The Dark Knight', 'Christopher Nolan', 2008, 'Action', 9.0)
    movie5 = Movie('Forrest Gump', 'Robert Zemeckis', 1994, 'Drama', 8.8)
    movie6 = Movie('The Godfather', 'Francis Ford Coppola', 1972, 'Crime', 9.2)


create()
