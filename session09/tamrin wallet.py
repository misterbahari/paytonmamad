class wallet:
    def __init__(self, **kwargs):
        self.bank_type = kwargs.get('bank', 'mellat')
        self.amount = 0

    def get_balance(self):
        return self.amount / 10


    def withdraw(self, price):
        self.amount += price * 10

    def deposit(self, price):
        condition, message = self.check_price_deposit(price)
        if condition:
            self.amount -= price * 10
            print(message)
        else:
            print(message)

    def check_price_deposit(self, price):
        if price > self.amount:
            return False, 'fail'
        return True , 'success'


wallet_mamareza = wallet()
wallet_mamareza.withdraw(250)
print(wallet_mamareza.amount)
# wallet_mamareza.deposit(35)
print(wallet_mamareza.get_balance())

print(wallet_mamareza.check_price_deposit(350))