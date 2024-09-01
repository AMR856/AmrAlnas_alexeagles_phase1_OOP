#!/usr/bin/env python3
from typing import List
from uuid import uuid4
from .employee import Employee
from .flight import Flight
from .meal import Meal
from .movie import Movie
from .dict_class import DictClass
from helpers.fixed_values import allowed_airlines


class Airline(DictClass):
    def __init__(self, airline_name: str,
                    employees: List[Employee],
                    services: List[Movie | Meal],
                    flights: List[Flight]) -> None:
        self.__airline_id = f'airline_{uuid4()}'
        self.airline_name = airline_name
        self.employees = employees
        self.services = services
        self.flights = flights

    @property
    def airline_id(self) -> str:
        return self.__airline_id

    @property
    def airline_name(self) -> str:
        return self.__airline_name
    
    @airline_name.setter
    def airline_name(self, value: str) -> None:
        if value not in allowed_airlines:
            raise ValueError('Airline name is not in the avaiable airlines in Egypt')
        self.__airline_name = value
    
    @property
    def employees(self) -> List[Employee]:
        return self.__employees

    @employees.setter
    def employees(self, value: List[Employee]):
        if value is None:
            self.__employees = []
            return
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Employee):
                    raise TypeError('Not all employees you gave me are real employees')
            self.__employees = value
        else:
            raise TypeError('You didn\t provide a list')

    def add_employee(self, value: Employee) -> None:
        if isinstance(value, Employee):
            self.__employees.append(value)
        else:
            raise TypeError('To add an employee you should give me an employee')

    def remove_employee(self, employee_name: str) -> None:
        status = 0
        if isinstance(employee_name, str):
            for employee in self.__employees:
                if employee.fullname == employee_name:
                    self.__employees.remove(employee)
                    status = 1
                    break
            if status:
                print('Employee was found and removed')
            else:
                print("Employee wasn't found")

    @property
    def services(self) -> List[Meal | Movie]:
        return self.__services
    
    @services.setter
    def services(self, value) -> None:
        if value is None:
            self.__services = []
            return
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Meal) and not isinstance(val, Movie):
                    raise TypeError('You should give me a meal or a movie')
            self.__services = value
        else:
            raise TypeError('You didn\t provide a list')

    def add_service(self, value: Meal | Movie) -> None:
        if isinstance(value, Meal) or isinstance(value, Movie):
            self.__services.append(value)
        else:
            raise TypeError('You should provdie a meal or movie object')

    def remove_service(self, service_name: str) -> None:
        status = 0
        if isinstance(service_name, str):
            for service in self.__services:
                if ((isinstance(service, Meal) and service.name) == service_name) or \
                    ((isinstance(service, Movie) and service.title) == service_name):
                    self.__employees.remove(service)
                    status = 1
                    break
            if status:
                print('Service was found and removed')
            else:
                print("Service wasn't found")

    @property
    def flights(self) -> List[Flight]:
        return self.__flights
    
    @flights.setter
    def flights(self, value) -> None:
        if value is None:
            self.__flights = []
            return
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Flight):
                    raise TypeError('You should give me a flight object')
            self.__flights = value
        else:
            raise TypeError('You didn\t provide a list')

    def add_flight(self, value: Flight) -> None:
        if isinstance(value, Flight):
            self.__flights.append(value)
        else:
            raise TypeError('You should provdie a flight object')

    def remove_flight(self, flight_id: str) -> None:
        status = 0
        if isinstance(flight_id, str):
            for flight in self.__flights:
                    if flight.flight_id == flight_id:
                        self.__flights.remove(flight)
                        status = 1
                        break
            if status:
                print('Service was found and removed')
            else:
                print("Service wasn't found")

    def __str__(self) -> str:
        employees_names = []
        services_names = []
        flights_id = []
        for employee in self.__employees:
            employees_names.append(employee.fullname)
        for service in self.__services:
            if isinstance(service, Meal):
                services_names.append(service.name)
            else:
                services_names.append(service.title)
        for flight in self.__flights:
            flights_id.append(flight.flight_id)
        return f"Airline's Name is {self.airline_name}\nEmployees Names are {employees_names}\nAvailable Services are {services_names}\nAnd the Available Flights IDs are {flights_id}"
