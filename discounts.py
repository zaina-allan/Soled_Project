from abc import ABC, abstractmethod

class IDiscount(ABC):
    
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


class FixedDiscount(IDiscount):
    
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount
    
    def apply_discount(self, amount: float) -> float:
        return amount - self.discount_amount


class PercentageDiscount(IDiscount):
    
    def __init__(self, percentage: float):
        self.percentage = percentage
    
    def apply_discount(self, amount: float) -> float:
        return amount - (amount * self.percentage / 100)
