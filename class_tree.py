import datetime
from typing import List, Union
from unicodedata import name

class Fish:
    
    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100

class FishShop:
    
    def add_fish(self, fish_name: str, total_weight: float) -> None:
        pass

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass
    
    def sell_fish(self, fish_name: str, weight: float) -> float:
        pass

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        pass

class Seller:

    def sell_fish(self, fish_name: str, fish_price_in_uah_per_kilo: float, 
                  fish_weight: float, is_fish_available_to_sell: bool) -> float:
        pass
    
class Buyer:

    def check_fish_list(self, fish_list: list(str) ) -> None:
        pass

    def check_fish_in_the_price_range(self, lower_price: float, higher_price: float) -> List[Union[str, float]]:
        pass

    def buy_fish(self, fish_name: str, fish_price_in_uah_per_kilo: float, 
                 fish_weight: float, catch_date: str ) -> None:
        pass
        
    
