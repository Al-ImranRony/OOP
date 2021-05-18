
class BankAcc:
    def __init__(self, name, bal=0):
        self.name = name
        self.bal = bal

    def display(self):
        print("Account: ", self.name)
        print("Balance: ", self.bal)

    def withdraw(self, amount):
        self.bal -= amount

    def deposit(self, amount):
        self.bal += amount

acc1 = BankAcc("Babu", 2000)
acc2 = BankAcc("Rony", 4)

acc1.display()
acc2.display()

print("After transactions in & out...\n")

acc1.withdraw(1000)
acc2.deposit(996)

acc1.display()
acc2.display()