import json
import os
from abc import ABC, abstractmethod
from bank_account import BankAccount


class Storage(ABC):

    @abstractmethod
    def save_data(self, accounts):
        ...
    
    @abstractmethod
    def load_data(self):
        ...


class JSONStorage(Storage):
    def __init__(self, file="db.json"):
        self.file = file
    
    def save_data(self, accounts):
        try: 
            with open(self.file, "w") as f:
                json.dump({number: account.to_dict() for number, account in accounts.items()}, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            if os.path.exists(self.file):
                with open(self.file, "r") as f:
                    data = json.load(f)
                    return {int(number): BankAccount.from_dict(account) for number, account in data.items()}
            return {}
        except FileNotFoundError:
            print("Data file not found, creating a new file.")
            return {}
        except json.JSONDecodeError:
            print("ERROR decoding the JSON file, please check the format.")
            return {}

class SQLStorage(Storage):
    def __init__(self, connection):
        self.connection = connection

    def save_data(self, accounts):
        # Logic to save accounts in the SQL database
        pass

    def load_data(self):
        # Logic to load accounts from the SQL database
        pass
