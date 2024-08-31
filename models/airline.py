#!/usr/bin/env python3
from typing import List
from .employee import Employee
from .meal import Meal
from .movie import Movie
from helpers.fixed_values import allowed_airlines


class Airline:
    # from .flight import Flight
    def __init__(self, airline_name: str,
                    employees: List[Employee],
                    services: List[Movie | Meal]) -> None:
        self.airline_name = airline_name
        self.employees = employees
        self.services = services

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
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Employee):
                    raise TypeError('Not all employees you gave me are real employees')
            self.__employees = value
        else:
            raise TypeError('You didn\t provide a list')

    @property
    def services(self) -> List[Meal | Movie]:
        return self.__services
    
    @services.setter
    def services(self, value) -> None:
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Meal) and not isinstance(val, Movie):
                    raise TypeError('You should give me a meal or a movie')
            self.__services = value
        else:
            raise TypeError('You didn\t provide a list')

    def __str__(self) -> str:
        return f'{self.airline_name}\nEmployees Count is {len(self.employees)}\nAvailable Services Count is {len(self.services)}'