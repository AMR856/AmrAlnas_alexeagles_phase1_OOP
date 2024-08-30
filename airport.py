#!/usr/bin/env python3
from typing import Tuple, List
from fixed_values import not_allowed_items_in_airports
from gate import Gate
import datetime

class Airport:
    not_allowed_items_in_airports = not_allowed_items_in_airports
    def __init__(self, airport_name: str,
                airport_location: str,
                airport_date_of_construction: Tuple[int],
                gates: List[Gate], 
                airport_size = Tuple[int],
                wifi_availability: bool = True
                ):
        self.airport_name = airport_name
        self.airport_location = airport_location
        self.airport_date_of_construction = airport_date_of_construction
        self.gates = gates
        self.airport_size = airport_size
        self.wifi_availability = wifi_availability

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
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Gate):
                    raise TypeError('Not all gates you gave me are real gates')
            self.__gates = value
        else:
            raise TypeError('You didn\t provide a list')

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
    def wifi_availability(self) -> bool:
        return self.__wifi_availability
    
    @wifi_availability.setter
    def wifi_availability(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__wifi_availability = value
        else:
            raise TypeError('You have to provide a boolean')
