from storage import Storage


class Bank:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.accounts = self.storage.load_data()
    
    def open_account(self, account):
        self.accounts[account.number] = account
        self.storage.save_data(self.accounts)
        print(f"Account {account.number} created successfully.")
    
    def deposit(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if account:
                account.deposit(amount)
                self.storage.save_data(self.accounts)
            else:
                print("Account not found.")
        except TypeError:
            print("Invalid amount provided for deposit.")

    def withdraw(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if account:
                account.withdraw(amount)
                self.storage.save_data(self.accounts)
            else:
                print("Account not found.")
        except ValueError:
            print("Invalid amount for withdrawal.")
        
    def display_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.display_balance()
        else:
            print("Account not found.")

    def delete_account(self, account_number):
        try:
            if account_number in self.accounts:
                del self.accounts[account_number]
                self.storage.save_data(self.accounts)
                print(f"Account {account_number} deleted successfully.")
            else:
                print(f"{account_number} not found.")
        except KeyError:
            print(f"Error: Account {account_number} does not exist.")
