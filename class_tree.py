import datetime
from typing import List, Union

class FishInfo:

    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime,
                origin: str, catch_date: datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.origin = origin
        self.catch_date = catch_date

class Fish:
    
    def __init__(self, weight: float, age_in_months: float) -> None:
        self.weight = weight
        self.age_in_months = age_in_months

class FishBox:

    def __init__ (self, fish_info: FishInfo, weight: float, package_date: datetime, 
                  height: float, lenght: float, width: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.lenght = lenght
        self.width = width
        self.is_alive = is_alive

class FishShop:
    def __init__(self, fish_boxes: dict[str: list[FishBox]], fresh_fish: dict[str: List[Fish]] ):
        self.fish_boxes = fish_boxes
        self.fresh_fish = fresh_fish

    def get_fish_names_sorted_by_price(self) -> list[list]:
        pass

    def add_fish(self, fish_box: FishBox) -> None:
        pass

    def add_fish(self, fish: Fish) -> None:
        pass

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> Union[str, float, float]:
        pass

    def get_frozen_fish_names_sorted_by_price(self) -> list[ tuple([str, bool, float]) ]:
        pass

    def get_fresh_fish_names_sorted_by_price(self) -> list[ tuple([str, bool, float]) ]:
        pass


    


    
        
    
