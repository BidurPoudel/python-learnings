from abc import ABC, abstractmethod
class PaymentProcess(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass
     
class PayPalProcessor(PaymentProcess):

    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")

class Stripe(PaymentProcess):
    def process_payment(self, amount: float):
        print(f"{amount} from stripe")

# this class is used to implement dependency injections
class ShoppingCart:
    def __init__(self, payment: PaymentProcess):
        self.processor = payment

    def checkout(self, amount: float):
        self.processor.process_payment(amount)

payment_process = PayPalProcessor()
stripe = Stripe()
cart = ShoppingCart(payment_process)
cart = ShoppingCart(stripe)
cart.checkout(100.0)

