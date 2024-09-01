#!/usr/bin/env python3
from typing import List
from uuid import uuid4

class Meal:
    def __init__(self, name: str,
                ingredients: List[str],
                calories: int) -> None:
        self.__meal_id = f'meal_{uuid4()}'
        self.name = name
        self.ingredients = ingredients
        self.calories = calories
    
    @property
    def meal_id(self) -> str:
        return self.__meal_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self.__name= value
        else:
            raise TypeError('You didn\t provide a string')

    @property
    def ingredients(self) -> List[str]:
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value: List[str]) -> None:
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, str):
                    raise TypeError('Not all ingredients you gave me are real ingredients')
            self.__ingredients = value
        else:
            raise TypeError('You didn\t provide a list of strings')

    @property
    def calories(self) -> int:
        return self.__calories
    
    @calories.setter
    def calories(self, value: int) -> None:
        if isinstance(value, int):
            self.__calories= value
        else:
            raise TypeError('You didn\t provide an integer')

    def __str__(self) -> str:
        return f"Meal's Name is {self.name}\nIts ingredients are {self.ingredients}\nIt contains {self.calories} Calories"
    