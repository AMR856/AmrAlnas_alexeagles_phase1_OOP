#!/usr/bin/env python3
from typing import Tuple, List
from fixed_values import not_allowed_items_in_airports
from gate import Gate

class Airport:
    def __init__(self, airport_name: str,
                airport_location: str,
                airport_date_of_construction: Tuple[int],
                gates: List[Gate], 
                airport_size = Tuple[int],
                wifi_availability: bool = True,
                currency : str = 'EP',
                ):
        pass
