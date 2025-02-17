# Exercise 1
import shelve
from datetime import datetime
import time
import random

class BankAccount:
    def __init__(self, account_id: int, full_name_owner: str, balance: float):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance
        self.creation_time = datetime.now()

    def __str__(self):
        return (f"Account ID: {self.account_id}, Owner: {self.full_name_owner}, "
                f"Balance: {self.balance}, Created: {self.creation_time}")

    def __repr__(self):
        return f"BankAccount('{self.account_id}', '{self.full_name_owner}', '{self.balance}')"

    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance == other
        if type(self) != type(other):
            return False
        return self.balance == other.balance

    def __ne__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance != other
        if type(self) != type(other):
            return False
        return self.balance != other.balance

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance > other
        if type(self) != type(other):
            return False
        return self.balance > other.balance

    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance > other
        if type(self) != type(other):
            return False
        return self.balance < other.balance

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance + other
        if type(self) != type(other):
            return self.balance
        return BankAccount(random.randint(self.account_id + other.account_id, self.account_id + other.account_id + 10),
        f'{self.full_name_owner} {other.full_name_owner}', self.balance + other.balance)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance - other
        if type(self) != type(other):
            return self.balance
        return self.balance - other.balance

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.balance * other
        if type(self) != type(other):
            return self.balance
        return self.balance * other.balance

    def __len__(self):
        time_diff = datetime.now() - self.creation_time
        return int(time_diff.total_seconds() // 60)

b1 = BankAccount(8676230, 'arya stark', 28000)
bg = BankAccount(6875533, 'golum', 28000)
b2 = BankAccount(5979982, 'jon snow', 79011)

print(b1)
print(repr(bg))
print(bg == b1)
print(b1 != bg)
print(b1 > b2)
print(b1 < b2)
b3 = b1 + b2
print(b3)
print(b2 - b1)
print(b2 * b1)

# Exercise 2
time.sleep(60)
minutes_elapsed = len(b1)
print(f"Account created at: {b1.creation_time}")
print(f"Account 1 has existed for {minutes_elapsed:.2f} minutes.")

# Exercise 3
sh = shelve.open('data.db')
sh['b1'] = b1
bank_account_1 = sh.get('b1')
print(bank_account_1)
sh.close()