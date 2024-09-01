#!/usr/bin/env python3
import sys
sys.path.append("..")
from typing import Tuple, List
from uuid import uuid4
from helpers.fixed_values import not_allowed_items_in_airports
from .employee import Employee
from .gate import Gate
import datetime

class Airport:
    not_allowed_items_in_airports = not_allowed_items_in_airports
    def __init__(self, airport_name: str,
                airport_location: str,
                airport_date_of_construction: Tuple[int],
                gates: List[Gate], 
                employees: List[Employee],
                airport_size = Tuple[int],
                wifi_availability: bool = True
                ):
        self.__airport_id = f'airport_{uuid4()}'
        self.airport_name = airport_name
        self.airport_location = airport_location
        self.airport_date_of_construction = airport_date_of_construction
        self.gates = gates
        self.airport_size = airport_size
        self.employees = employees
        self.wifi_availability = wifi_availability


    @property
    def airport_id(self) -> str:
        return self.__airport_id
    
    @property
    def airport_name(self) -> str:
        return self.__airport_name
    
    @airport_name.setter
    def airport_name(self, value: str) -> None:
        if isinstance(value, str):
            self.__airport_name = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def airport_location(self) -> str:
        return self.__airport_location
    
    @airport_location.setter
    def airport_location(self, value: str) -> None:
        if isinstance(value, str):
            self.__airport_location = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def airport_date_of_construction(self) -> str:
        return (self.__airport_date_of_constructione).strftime("%x")

    @airport_date_of_construction.setter
    def airport_date_of_construction(self, value: Tuple[int]) -> None:
        if isinstance(value, tuple) and len(value) == 3:
            for val in value:
                if not isinstance(val, int):
                    raise TypeError('The date is not correct')
            year, month, day = value
            self.__airport_date_of_constructione = datetime.datetime(year, month, day)
        else:
            raise ValueError('Some values are missing or tuple wasn\t given')

    @property
    def gates(self) -> List[Gate]:
        return self.__gates
    
    @gates.setter
    def gates(self, value: List[Gate]) -> None:
        if value is None:
            self.__gates = []
            return
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Gate):
                    raise TypeError('Not all gates you gave me are real gates')
            self.__gates = value
        else:
            raise TypeError('You didn\t provide a list')

    def add_gate(self, value: Gate) -> None:
        if isinstance(value, Gate):
            self.__employees.append(value)
        else:
            raise TypeError('To add a gate you should give me a gate')

    def remove_gate(self, gate_number: int) -> None:
        status = 0
        if isinstance(gate_number, int):
            for gate in self.__gates:
                if gate.gate_number == gate_number:
                    self.__employees.remove(gate)
                    status = 1
                    break
            if status: 
                print('Gate was found and removed')
            else:
                print("Gate wasn't found")

    @property
    def airport_size(self) -> Tuple[int]:
        return self.__airport_size
    
    @airport_size.setter
    def airport_size(self, value: Tuple[int]) -> None:
        if isinstance(value, tuple) and len(value) == 2:
            for val in value:
                if not isinstance(val, int):
                    raise TypeError('The size is not correct')
            self.__length = value[0]
            self.__width = value[1]
            self.__airport_size = value
        else:
            raise ValueError('Some values are missing or tuple wasn\' given')

    @property
    def length(self) -> int:
        return self.__length

    @property
    def width(self) -> int:
        return self.__width

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
    def wifi_availability(self) -> bool:
        return self.__wifi_availability
    
    @wifi_availability.setter
    def wifi_availability(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__wifi_availability = value
        else:
            raise TypeError('You have to provide a boolean')

    def __str__(self) -> str:
        gates_numbers = []
        employees_names = []
        for gate in self.__gates:
            gates_numbers.append(gate.gate_number)
        for employee in self.__employees:
            employees_names.append(employee.fullname)
        return f'{self.airport_name}\nAirport Location is {self.airport_location}\nAirport Date of Construction is {self.airport_date_of_construction}\nGates Numbers are {gates_numbers}\nAirport Size is {self.airport_size}\nEmployees Names are {employees_names}\nWifi is {"Available" if self.wifi_availability else "Not Available"}'
