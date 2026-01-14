# ATM Project with File Handling and Safe Input

# ---------- Helper Functions ----------

def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except:
            print("Invalid input. Please enter a number.")


def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                name, balance = line.strip().split(":")
                accounts[name] = Account(name, int(balance))
    except:
        pass   # If file not found, start with empty accounts
    return accounts


def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for name, acc in accounts.items():
            file.write(f"{name}:{acc.balance}\n")


# ---------- Account Class ----------

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")


# ---------- Main Program ----------

accounts = load_accounts()

print("==== Welcome to Simple ATM ====")

name = input("Enter your name: ")

if name not in accounts:
    print("New account created.")
    accounts[name] = Account(name, 0)

user = accounts[name]

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = get_int_input("Enter choice: ")

    if choice == 1:
        amount = get_int_input("Enter amount to deposit: ")
        user.deposit(amount)

    elif choice == 2:
        amount = get_int_input("Enter amount to withdraw: ")
        user.withdraw(amount)

    elif choice == 3:
        user.show_balance()

    elif choice == 4:
        save_accounts(accounts)
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice")
