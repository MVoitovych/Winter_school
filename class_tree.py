import datetime
from typing import List, Union

class FishInfo:

    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime,
                origin: str, catch_date: datetime) -> None:
        pass

class Fish:
    
    def __init__(self, weight: float, age_in_months: float) -> None:
        pass

class FishBox:
    def __init__ (self, fish_info: FishInfo, weight: float, package_date: datetime, 
                  height: float, lenght: float, width: float, is_alive: bool) -> None:
        pass

class FishShop:
    def __init__(self, fish_boxes: dict[str: list[FishBox]], fresh_fish: dict[str: List[Fish]] ):
        pass

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



    


    
        
    
