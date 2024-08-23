# main.py
from discounts import PercentageDiscount
from discounts import FixedDiscount
#from transaction_logger import *
#from currency_converter import *
from Pyment_Methodes import *

# logging/transaction_logger.py
import datetime

# currency/currency_converter.py
class CurrencyConverter:
    
    def __init__(self):
        self.exchange_rates = {
            "USD": 1,
            "EUR": 0.85,
            "GBP": 0.75
        }
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency != "USD":
            amount = amount / self.exchange_rates[from_currency]
        return amount * self.exchange_rates[to_currency]


class TransactionLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TransactionLogger, cls).__new__(cls)
            cls._instance.log_file = 'transactions.log'
        return cls._instance
    
    def log(self, message: str):
        with open(self.log_file, 'a') as file:
            file.write(f"{datetime.datetime.now()}: {message}\n")

def main():
    logger = TransactionLogger()
    converter = CurrencyConverter()
    
    # Process Credit Card Payment
    credit_payment = CreditCardPayment("1234-5678-9876-5432", "12/24", "123")
    amount = converter.convert(100, "USD", "EUR")
    amount_with_discount = PercentageDiscount(10).apply_discount(amount)
    if credit_payment.process_payment(amount_with_discount):
        logger.log(f"Credit Card payment of {amount_with_discount} EUR processed.")
    
    # Process PayPal Payment
    paypal_payment = PayPalPayment("user@example.com")
    amount = 50
    amount_with_discount = FixedDiscount(5).apply_discount(amount)
    if paypal_payment.process_payment(amount_with_discount):
        logger.log(f"PayPal payment of {amount_with_discount} USD processed.")
    
    # Process Crypto Payment
    crypto_payment = CryptoPayment("wallet_address")
    amount = 0.005
    if crypto_payment.process_payment(amount):
        logger.log(f"Cryptocurrency payment of {amount} BTC processed.")

if __name__ == "__main__":
    main()
