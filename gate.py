#!/usr/bin/env python3
from typing import Tuple

class Gate:
    def __init__(self,
                gate_number: int,
                gate_location: str,
                gate_allowed_passing_people: int,
                gate_size: Tuple[int]) -> None:
        self.gate_number = gate_number
        self.gate_location = gate_location
        self.gate_allowed_passing_people = gate_allowed_passing_people
        self.gate_size = gate_size
    
    @property
    def gate_number(self) -> int:
        return self.__gate_number
    
    @gate_number.setter
    def gate_number(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__gate_number = value
        else:
            raise TypeError('You have to provide an integer bigger than or equal to 0')
    
    @property
    def gate_location(self) -> str:
        return self.__gate_location
    
    @gate_location.setter
    def gate_location(self, value: str) -> None:
        if isinstance(value, str):
            self.__gate_number = value
        else:
            raise TypeError('You have to provide a string to the location')

    @property
    def gate_allowed_passing_people(self) -> int:
        return self.__gate_allowed_passing_people
    
    @gate_allowed_passing_people.setter
    def gate_allowed_passing_people(self, value: int) -> None:
        if isinstance(value, int) and value >= 2:
            self.__gate_allowed_passing_people = value
        else:
            raise TypeError('You have to provide an integer with a logical \
size of the gate')

    @property
    def gate_size(self) -> Tuple[int]:
        return self.__gate_size
    
    @gate_size.setter
    def gate_size(self, value) -> None:
        if isinstance(value, tuple) and len(value) == 2:
            for val in value:
                if not isinstance(val, int):
                    raise TypeError('The size is not correct')
            self.__length = value[0]
            self.__width = value[1]
            self.__gate_size = value
        else:
            raise ValueError('Some values are missing or tuple wasn\t given')

    @property
    def length(self) -> int:
        return self.__length

    @property
    def width(self) -> int:
        return self.__width
