class Bank:

    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance


account = Bank()

print(account.get_balance())