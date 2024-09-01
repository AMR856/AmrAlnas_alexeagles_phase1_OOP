#!/usr/bin/env python3
from re import I

from validators import isin
from .person import Person
from .flight import Flight
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
        if value is None:
            self.__flights = []
            return
        if isinstance(value, list):
            for flight in value:
                if not isinstance(flight, Flight):
                    raise TypeError('Not all flights you gave me are real flights')
            self.__flights = value
        else:
            raise TypeError('You didn\t provide a list')

    def add_flight(self, value = Flight) -> None:
        if isinstance(value, Flight):
            if not self.__flights:
                self.__flights = []
            self.__flights.append(value)
        else:
            raise TypeError("Are you kidding me?")

    def remove_budget(self, value: int) -> None:
        if isinstance(value, int):
            self.__budget -= value
        else:
            raise TypeError("Can't remove anything except int")

    def add_budget(self, value: int) -> None:
        if isinstance(value, int):
            self.__budget += value
        else:
            raise TypeError("Can't add anything except int")

    def __str__(self) -> str:
        customers_flights_ids = []
        for flight in self.__flights:
            customers_flights_ids.append(flight.flight_id)
        return f"Customer's Name is {self.fullname}\nBirthdate is {self.birthdate}\nAddress is {self.address}\nCustomer's Email is {self.email}\nHis Budget is {self.budget}\nAnd Booked {customers_flights_ids} Flights"
