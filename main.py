from bank_account import BankAccount, CheckingAccount, SavingsAccount
from bank import Bank
from storage import JSONStorage

# Initializing the system with JSON storage
storage = JSONStorage("db.json")
my_bank = Bank(storage)

# Creating and opening accounts
account1 = BankAccount("Pedro", 105752, 12345678911, balance=2000)
my_bank.open_account(account1)

current_account = CheckingAccount("Joao", 656963, 45263852000, balance=2500)
my_bank.open_account(current_account)

my_bank.withdraw(656963, 500)
# my_bank.delete_account(656963)

# Operations
# my_bank.deposit(105752, 500)
# my_bank.display_balance(105752)
my_bank.withdraw(105752, 100)
# my_bank.display_balance(105752)
# my_bank.delete_account(105752)
