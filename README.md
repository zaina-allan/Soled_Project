1. Architecture Overview

The payment processing system is organized into several modules, each with its own responsibility:

    payment_methods/: Contains different payment method implementations, each conforming to a common interface.
    discounts/: Contains discount types that can be applied to payments. Each discount class implements a common interface.
    logging/: Contains a singleton logger for transaction logging.
    currency/: Contains a currency conversion service to handle payments in different currencies.
    main.py: The entry point for the application where the payment process is orchestrated.
    tests/: Contains unit tests for different components to ensure the correctness of the implementation.

2. Design Patterns Used

    Strategy Pattern: Used in the payment_methods module to define a family of payment algorithms (e.g., Credit Card, PayPal, Cryptocurrency), encapsulate each one, and make them interchangeable. This pattern allows the payment processing system to support multiple payment methods without changing its core logic.

    Decorator Pattern: Applied in the discounts module, allowing for dynamic addition of discount behaviors to a payment amount. The discount classes wrap the payment amount and modify its value, enabling flexible discount handling without altering the payment processing logic.

    Singleton Pattern: Implemented in the logging module to ensure only one instance of the TransactionLogger exists throughout the application. This pattern is essential for consistency in logging across the application.

    Factory Pattern (implicit): Although not explicitly implemented as a separate factory class, the architecture lends itself to a factory pattern where different payment methods and discounts could be instantiated based on external input (e.g., user choice). This can be easily added if needed.

    Dependency Injection (DI): Demonstrated in how the CurrencyConverter can be injected into payment methods if needed, making the system more modular and easier to test.

