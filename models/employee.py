#!/usr/bin/env python3
import sys
sys.path.append("..")
from .dict_class import DictClass
from .person import Person
from typing import Tuple
from helpers.fixed_values import allowed_airlines
from helpers.helper_functions import map_range
import re

lower_value_allowed_airlines = list(map(str.lower, allowed_airlines))

class Employee(Person, DictClass):
    def __init__(self, firstname: str,
                lastname: str,
                birthdate: Tuple[int],
                email: str,
                start_hour: str,
                finish_hour: str,
                salary: int,
                airline_name: str,
                address: str = 'Somewhere in Egypt'):
        super().__init__(firstname, lastname, birthdate, email, address)
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.salary = salary
        self.airline_name = airline_name

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value: int):
        if isinstance(value, int) and value >= 5000:
            self.__salary = value
        else:
            raise TypeError('You should provide the salary as an integer, \
and with a resonable value')

    @property
    def airline_name(self):
        return self.__airline_name
    
    @airline_name.setter
    def airline_name(self, value: str):
        allowed_airlines_lower = list(map(str.lower, allowed_airlines))
        if isinstance(value, str):
            if value.lower() in allowed_airlines_lower:
                self.__airline_name = value
            else:
                raise ValueError("You can't work there because it doesn't exist")
        else:
            raise TypeError('You should provide a string')

    @property
    def start_hour(self):
        return self.__start_hour
    
    @start_hour.setter
    def start_hour(self, value: str):
        if isinstance(value, str) and re.match(r'^\d?\d:\d{2} (PM|AM)$', value):
            self.__start_hour = value
        else:
            raise TypeError('You should provide a correct time format')

    @property
    def finish_hour(self):
        return self.__finish_hour
    
    @finish_hour.setter
    def finish_hour(self, value: str):
        if isinstance(value, str) and re.match(r'^\d?\d:\d{2} (PM|AM)$', value):
            self.__finish_hour = value
        else:
            raise TypeError('You should provide a correct time format')
    
    @property
    def working_hours(self):
        start_time, start_timezone = (self.__start_hour).split(' ')
        finish_time, finish_timezone = (self.__finish_hour).split(' ')
        start_hour, start_minute = start_time.split(':')
        finish_hour, finish_minute = finish_time.split(':')
        if start_timezone == 'PM':
            start_hour = str(int(start_hour) + 12)
        if finish_timezone == 'PM':
            finish_hour = str(int(finish_hour) + 12)
        working_hours = int(finish_hour) - int(start_hour)
        if int(start_minute) > int(finish_minute):
            working_hours -= (int(start_minute) - int(finish_minute)) / 60
        else:
            working_hours += (int(start_minute) - int(finish_minute)) / 60
        working_hours, number_after_digit = str(working_hours).split('.')
        if number_after_digit:
            number_after_digit = int(map_range(int(number_after_digit), 0, 10, 0, 60))
        return f'{working_hours}:{number_after_digit} Hours'

    def salary_raise(self, value: int) -> None:
        if isinstance(value, int):
            self.__salary += value
        else:
            raise TypeError("Can't raise salary with non-integer value")

    def __str__(self) -> str:
        return f"Employee's Start Hour is {self.start_hour} and Finish Hour is {self.finish_hour}\nHis Salary is {self.salary}\nHis Woring Hours in Total is {self.working_hours}\nAnd the Airline he is working in is {self.airline_name}"
