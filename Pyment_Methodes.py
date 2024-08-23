
import unittest
import re
from abc import ABC, abstractmethod

class IPaymentMethod(ABC):
    
    @abstractmethod
    def validate(self) -> bool:
        pass
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCardPayment(IPaymentMethod):
    
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
    
    def validate(self) -> bool:
        # Validate card number (simple regex check)
        if not re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', self.card_number):
            print("Invalid card number")
            return False
        
        # Validate expiry date (format MM/YY)
        if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', self.expiry):
            print("Invalid expiry date")
            return False
        
        # Validate CVV (3 digits)
        if not re.match(r'^\d{3}$', self.cvv):
            print("Invalid CVV")
            return False
        
        return True
    
    def process_payment(self, amount: float) -> bool:
        if self.validate():
            print(f"Processing credit card payment of {amount}")
            return True
        return False

#from payment_methods.ipayment_method import IPaymentMethod

class CryptoPayment(IPaymentMethod):
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def validate(self) -> bool:
        # Validate wallet address (basic length and format check)
        if not re.match(r'^[a-zA-Z0-9]{26,35}$', self.wallet_address):
            print("Invalid cryptocurrency wallet address")
            return False
        
        return True
    
    def process_payment(self, amount: float) -> bool:
        if self.validate():
            print(f"Processing cryptocurrency payment of {amount}")
            return True
        return False
    
class PayPalPayment(IPaymentMethod):
    
    def __init__(self, email: str):
        self.email = email
    
    def validate(self) -> bool:
        # Validate email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email):
            print("Invalid email address")
            return False
        
        return True
    
    def process_payment(self, amount: float) -> bool:
        if self.validate():
            print(f"Processing PayPal payment of {amount}")
            return True
        return False
class TestCreditCardPayment(unittest.TestCase):
    
    def test_invalid_card_number(self):
        payment = CreditCardPayment("1234", "12/24", "123")
        self.assertFalse(payment.validate())

    def test_invalid_expiry_date(self):
        payment = CreditCardPayment("1234-5678-9876-5432", "13/24", "123")
        self.assertFalse(payment.validate())
    
    def test_invalid_cvv(self):
        payment = CreditCardPayment("1234-5678-9876-5432", "12/24", "12")
        self.assertFalse(payment.validate())

class TestPayPalPayment(unittest.TestCase):
    
    def test_invalid_email(self):
        payment = PayPalPayment("invalid-email")
        self.assertFalse(payment.validate())

class TestCryptoPayment(unittest.TestCase):
    
    def test_invalid_wallet_address(self):
        payment = CryptoPayment("invalid_wallet_address!")
        self.assertFalse(payment.validate())

if __name__ == '__main__':
    unittest.main()
