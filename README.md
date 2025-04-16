Bank Management System

This is a simple object-oriented banking system written in Python. It allows you to manage customer bank accounts and perform basic operations like account creation, deposit, withdrawal, and viewing account info.


---

✅ Main Features:

1. Account Management:

Each account has:

Account holder name

Account number

Current balance


You can:

Create a new account

Deposit money into an account

Withdraw money (if the balance is enough)

View account details

Check balance



---

2. Account Class (BankAccount):

The BankAccount class stores individual customer data:

It has variables: name, acc_num, balance

It has methods:

deposit(): Adds amount to balance

withdraw(): Subtracts amount if enough balance exists

display(): Shows account info



This class ensures encapsulation — the data is handled internally by the class itself.


---

3. Bank System Logic (Main Menu Loop):

The system shows a simple menu where the user can:

1. Create account


2. Deposit money


3. Withdraw money


4. Display account info


5. Exit



Each menu choice runs a specific function.


---

4. Data Management:

Accounts are stored in a dictionary (accounts) where the key is the account number.

It checks if an account already exists before creating one.

All logic is in memory only (no database or file saving yet).



---

🧠 Concepts Used:

Object-Oriented Programming (OOP):

Classes: BankAccount

Objects: Each account is an object of the class


Encapsulation:

Deposit and withdrawal logic is built inside the class


Input Validation:

You can't withdraw more than the available balance

Prevents duplicate account numbers


Loop and Conditionals:

Menu is shown using a while loop

Functions are selected using if-elif conditions




---

🛠️ Potential Uses:

Can be used for:

School/college projects

Practice for beginners in Python

Small-scale banking simulation



Can be extended with:

File or database support (e.g., saving data to a file)

GUI interface using Tkinter or PyQt

Web version using Flask or Django

Login system for users and admins
