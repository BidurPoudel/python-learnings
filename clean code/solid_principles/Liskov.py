
class Payment:
    def process_payment(self, amount):
        pass


class CreditPayment(Payment):
    def process_payment(self, amount):
        print(f"Process credit card payment of {amount}")


class CashPayment(Payment):
    def process_payment(self, amount):
        raise Exception("Cannot process cash Payment")


def process_payment(order_amount,  payment_method: Payment):
    payment_method.process_payment(order_amount)



credit_payment = CreditPayment()
cash_payment = CashPayment()
