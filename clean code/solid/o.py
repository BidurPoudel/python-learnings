# open for extension close for modification



# bad example

# class DiscountCalculator:
#     def calculate(self, user_type:str):
#         if user_type=='member':
#             return 12
#         elif user_type=='premium':
#             return 13


# good practice
from abc import ABC, abstractmethod
class Discount(ABC):
    
    @abstractmethod
    def calculate(self):
        pass

class RegularDiscount(Discount):
    def calculate(self):
        return 12


class PremiumDiscount(Discount):
    def calculate(self):
        return 6