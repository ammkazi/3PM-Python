#Simple Banking System

class Bank:

    def __init__(self, name, accountno, balance):
       
        self.name = name
        self.accountno = accountno
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance + amount
        print("Amount deposited , Current balance is:  ₹" , self.balance)

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insufficient amount")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn\nCurrent Balance: ₹", self.balance)

    def display(self):
        print("Account Holder Name: " + self.name)
        print("Account ID: " , self.accountno)
        print("Balance: " , self.balance)


# Creating objects

acc1 = Bank("Sahil", 101, 5000)

acc1.deposit(2000)
acc1.withdraw(3000)

acc1.display()

acc2 = Bank("Kaif", 102, 10000)
acc2.display()