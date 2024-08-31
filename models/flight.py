#!/usr/bin/env python3
import datetime
import uuid
from models.airline import Airline

class Flight:
    def __init__(self, flight_id: uuid.UUID,
                departure_time: datetime.datetime,
                arrival_time: datetime.datetime,
                from_place: str,
                to_place: str,
                price: int) -> None:
        self.flight_id = flight_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.from_place = from_place
        self.to_place = to_place
        self.price = price

    @property
    def flight_id(self) -> str:
        return str(self.__flight_id)
    
    @flight_id.setter
    def flight_id(self, value: uuid.UUID) -> None:
        if isinstance(value, uuid.UUID):
            self.__flight_id = value
        else:
            raise TypeError('You have to provide a uuid.UUID object')

    @property
    def departure_time(self) -> str:
        return (self.__departure_time).strftime("%c")
    
    @departure_time.setter
    def departure_time(self, value: datetime.datetime) -> None:
        if isinstance(value, datetime.datetime):
            self.__departure_time = value
        else:
            raise TypeError('You have to provide a datetime.datetime object')
    
    @property
    def arrival_time(self) -> str:
        return (self.__arrival_time).strftime("%c")
    
    @arrival_time.setter
    def arrival_time(self, value: datetime.datetime) -> None:
        if isinstance(value, datetime.datetime):
            self.__arrival_time = value
        else:
            raise TypeError('You have to provide a datetime.datetime object')

    @property
    def from_place(self) -> str:
        return self.__from_place
    
    @from_place.setter
    def from_place(self, value: str) -> None:
        if isinstance(value, str):
            self.__from_place = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def to_place(self) -> str:
        return self.__to_place
    
    @to_place.setter
    def to_place(self, value: str) -> None:
        if isinstance(value, str):
            self.__to_place = value
        else:
            raise TypeError('You have to provide a string')

    @property
    def price(self) -> int:
        return self.__price
    
    @price.setter
    def price(self, value: int) -> None:
        if isinstance(value, int):
            self.__price= value
        else:
            raise TypeError('You have to provide an int')

    def __str__(self) -> str:
        return f"Flight's ID is {self.flight_id}\nDeparture Time is {self.departure_time}\nArrival Time {self.arrival_time}\nIt's going from {self.from_place} to {self.to_place}\nIt costs {self.price}"
