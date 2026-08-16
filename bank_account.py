class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Create account
account = BankAccount("Manasa", 5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1000)
account.display_balance()