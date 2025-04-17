import os

class BankAccount:
    def __init__(self, name, acc_num, balance=0):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acc_num}")
        print(f"Balance: {self.balance}")

# Dictionary to store account info (in memory)
accounts = {}

def create_account():
    name = input("Enter account holder name: ")
    acc_num = input("Enter new account number: ")
    if acc_num in accounts:
        print("Account already exists.")
        return
    account = BankAccount(name, acc_num)
    accounts[acc_num] = account
    print("Account created successfully.")

def deposit_amount():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num].deposit(amount)
    else:
        print("Account not found.")

def withdraw_amount():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[acc_num].withdraw(amount)
    else:
        print("Account not found.")

def display_account():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        accounts[acc_num].display()
    else:
        print("Account not found.")

# Main Menu
while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Display Account Info")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_amount()
    elif choice == '3':
        withdraw_amount()
    elif choice == '4':
        display_account()
    elif choice == '5':
        print("Thank you for using the system.")
        break
    else:
        print("Invalid choice. Please try again.")
        
#Working example 

account1=BankAccont("Muhammad Danish", '5432', 0) 
print (accunt1. deposit (1000) ) 
print (accunt1. withdraw (1000) )
accunt1. display() 


