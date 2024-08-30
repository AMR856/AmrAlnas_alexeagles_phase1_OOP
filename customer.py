#!/usr/bin/env python3
from person import Person
from flight import Flight
from typing import Tuple, List

class Customer(Person):
    def __init__(
            self, firstname: str,
                lastname: str,
                birthdate: Tuple[int],
                email: str,
                budget: int,
                flights: List[Flight] | None = None,
                address: str = 'Somewhere in Egypt'):
        super().__init__(firstname, lastname, birthdate, email, address)
        self.budget = budget
        self.flights = flights

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value: int):
        if isinstance(value, int) and value >= 0:
            self.__budget = value
        else:
            raise TypeError('You can\'t be in debt and try to book a flight\
broke little boy')

    @property
    def flights(self):
        return self.__flights

    @flights.setter
    def flights(self, value: List[Flight] | None):
        for flight in value:
            if not isinstance(flight, Flight):
                raise TypeError('Not flights you gave me are real flights')
        self.__flights = value
