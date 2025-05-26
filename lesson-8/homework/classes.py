# Farm Model

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def moo(self):
        return f"{self.name} says Moo!"

class Chicken(Animal):
    def lay_egg(self):
        return f"{self.name} laid an egg."

class Pig(Animal):
    def oink(self):
        return f"{self.name} says Oink!"

# Bank Application
import json
import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(6)
        if initial_deposit < 0:
            return "Initial deposit must be non-negative."
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created. Number: {account_number}"

    def view_account(self, account_number):
        acc = self.accounts.get(account_number)
        if acc:
            return f"Account Number: {acc.account_number}, Name: {acc.name}, Balance: ${acc.balance:.2f}"
        return "Account not found."

    def deposit(self, account_number, amount):
        if amount <= 0:
            return "Deposit must be positive."
        acc = self.accounts.get(account_number)
        if acc:
            acc.balance += amount
            self.save_to_file()
            return f"Deposited ${amount:.2f}. New balance: ${acc.balance:.2f}"
        return "Account not found."

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if not acc:
            return "Account not found."
        if amount <= 0:
            return "Withdrawal must be positive."
        if amount > acc.balance:
            return "Insufficient funds."
        acc.balance -= amount
        self.save_to_file()
        return f"Withdrawn ${amount:.2f}. New balance: ${acc.balance:.2f}"

    def save_to_file(self):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open("accounts.txt", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        if not os.path.exists("accounts.txt"):
            return
        with open("accounts.txt", "r") as f:
            data = json.load(f)
            for acc_no, acc_data in data.items():
                self.accounts[acc_no] = Account(**acc_data)

# Example Usage
if __name__ == "__main__":
    bank = Bank()
    print(bank.create_account("Alice", 1000))
    print(bank.view_account("000001"))
    print(bank.deposit("000001", 500))
    print(bank.withdraw("000001", 200))

    # Farm example
    cow = Cow("Bessie", 5)
    chicken = Chicken("Cluck", 2)
    pig = Pig("Porky", 3)
    print(cow.moo())
    print(chicken.lay_egg())
    print(pig.oink())
