#!/usr/bin/env python3
import sys
sys.path.append("..")
import datetime
import validators
from typing import Tuple
from .dict_class import DictClass
from uuid import uuid4

class Person(DictClass):
    def __init__(self, firstname: str,
                lastname: str,
                birthdate: Tuple[int],
                email: str,
                address: str = 'Somewhere in Egypt') -> None:
        self.__person_id = None
        self.__customer_id = None
        self.__employee_id = None
        if self.__class__.__name__ == 'Person':
            self.__person_id = f'person_{uuid4()}'
        elif self.__class__.__name__ == 'Employee':
            self.__employee_id = f'employee_{uuid4()}'
        else:
            self.__customer_id = f'customer_{uuid4()}'
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address= address
        self.email = email

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def person_id(self) -> str:
        return self.__person_id

    @property
    def firstname(self) -> str:
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        if isinstance(value, str):
            self.__firstname = value
        else:
            raise TypeError('You should provide the firstname as a str')

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        if isinstance(value, str):
            self.__lastname = value
        else:
            raise TypeError('You should provide the lastname as a str')
    
    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, value: str) -> None:
        if isinstance(value, str):
            self.__address = value
        else:
            raise TypeError('You should provide the address as a str')

    @property
    def birthdate(self) -> str:
        return self.__birthdate.strftime("%x")

    @birthdate.setter
    def birthdate(self, value: Tuple[int]) -> None:
        if isinstance(value, tuple) and len(value) == 3:
            for val in value:
                if not isinstance(val, int):
                    raise TypeError('The date is not correct')
            year, month, day = value
            self.__birthdate = datetime.datetime(year, month, day)
        else:
            raise ValueError('Some values are missing or tuple wasn\t given')

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, value: str) -> None:
        if isinstance(value, str):
            if validators.email(value):
                self.__email = value
            else:
                raise ValueError('Email is not correct')
        else:
            raise TypeError('You should provide a string email')

    @property
    def fullname(self) -> str:
        return (self.firstname + ' ' + self.lastname)


    def __str__(self) -> str:
        return f"Person's Name is {self.fullname}\nBirthdate is {self.birthdate}\nAddress is {self.address}\nPerson's Email is {self.email}"
