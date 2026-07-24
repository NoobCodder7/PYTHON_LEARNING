from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment successful using UPI.")


class CreditCard(Payment):

    def pay(self):
        print("Payment successful using Credit Card.")


class PayPal(Payment):

    def pay(self):
        print("Payment successful using PayPal.")


upi = UPI()
card = CreditCard()
paypal = PayPal()

upi.pay()
card.pay()
paypal.pay()