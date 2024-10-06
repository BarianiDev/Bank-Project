class BankAccount:
    def __init__(self, name, number, cpf, balance=0):  # Implementing encapsulation here
        self._name = name
        self._number = number
        self._cpf = cpf
        self._balance = balance

    # Implementing getters and setters for accessing data

    @property
    def name(self):
        return self._name
    
    @property
    def number(self):
        return self._number
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def balance(self):
        return self._balance
    
    # Setter for the balance
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative.")
    

    def __repr__(self):
        return f"BankAccount(name={self.name}, number={self.number}, cpf={self.cpf})"

    def deposit(self, value):
        if value > 0:
            self.balance += value
            print(f"The deposit of R${value:.2f} was successfully completed.")
        else:
            print("Invalid deposit amount.")

    
    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            print(f"You withdrew R${value:.2f} from the account.")
        else:
            print("Insufficient funds.")
        
    
    def display_balance(self):
        print(f"Your balance is R${self.balance:.2f}")

    def to_dict(self):
        return {
            "Name": self.name,
            "Number": self.number,
            "CPF": self.cpf,
            "Balance": self.balance
        }
    
    @staticmethod
    def from_dict(data):
        return BankAccount(data["Name"], data["Number"], data["CPF"], data["Balance"])


class CheckingAccount(BankAccount):
    def __init__(self, name, number, cpf, balance=0, withdrawal_fee=5):
        super().__init__(name, number, cpf, balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, value):
        # Adds a fee to the amount to be withdrawn
        total_value = value + self.withdrawal_fee
        if total_value <= self.balance:
            self.balance -= total_value
            print(f"You withdrew R${value:.2f} with a fee of R${self.withdrawal_fee:.2f}. Total withdrawn R${total_value:.2f}.")
        else:
            print("Insufficient funds.")


class SavingsAccount(BankAccount):
    def __init__(self, name, number, cpf, balance=0, withdrawal_limit=1000):
        super().__init__(name, number, cpf, balance)
        self.limit = withdrawal_limit
    
    def withdraw(self, value):
        if value > self.limit:
            print(f"You cannot withdraw more than R${self.limit:.2f} per day.")
        elif value <= self.balance:
            self.balance -= value
            print(f"You withdrew R${value:.2f}.")
        else:
            print("Insufficient funds.")
